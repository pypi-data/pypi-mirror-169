from typing import Optional
import typer

try:
    from .utils import *
    from .logs import get_logger, get_rich_console
    from .nodes import ServiceNode
    from .reader import ServiceReader
    from .custom_nodes import *
except ImportError:
    from utils import *
    from logs import get_logger, get_rich_console
    from nodes import ServiceNode
    from reader import ServiceReader
    from custom_nodes import *

import boto3
from rich.columns import Columns
from rich.panel import Panel
from rich.console import Console
from rich.layout import Layout
from rich.pretty import Pretty
import os

def _create_boto_session():
    profile_name = os.environ.get('AWS_PROFILE', False)
    region_name = os.environ.get('AWS_REGION', False)
    _kwargs_dict = {}
    if profile_name:
        _kwargs_dict['profile_name']=profile_name
    if region_name:
        _kwargs_dict['region_name']=region_name
    session = boto3.session.Session(**_kwargs_dict)
    return session 

console = get_rich_console()
logger = get_logger(__name__)
session = _create_boto_session()

app = typer.Typer(no_args_is_help=True)
aws_app = typer.Typer() # no_args_is_help=True
app.add_typer(aws_app, name="aws")
# aws_ls_app = typer.Typer(no_args_is_help=True)
# aws_app.add_typer(aws_ls_app, name="ls")

def _get_available_service_node_names():
    return get_all_available_services(session)

def generate_service_node_completion_items():
    service_names = _get_available_service_node_names(session)
    return service_names

def _complete_service_name(incomplete: str):
    service_names = _get_available_service_node_names()
    if not incomplete:
        for name in service_names:
            yield name
    else:
        for name in service_names:
            if name.startswith(incomplete):
                yield name

from rich import inspect
err_console = Console(stderr=True)
def _complete_resource_node_name(ctx: typer.Context, incomplete: str):
    err_console.print(f"{inspect(ctx)}")
    service = ctx.params.get("service") or False
    if not service:
        return ["no service"]
    service_node = ServiceNode(service, session)
    if not service_node:
        return ["no service node" ]
    resource_nodes = service_node.get_resource_nodes()
    if not resource_nodes:
        return ["no resource node"]
    
    if incomplete:
        for _rn in resource_nodes:
            _rn_name = _rn.name
            if _rn_name.startswith(incomplete):
                # if _rn.get_all_required_parameter_names():
                #     _rn_name = f"[bold]{_rn_name}[/]"
                yield _rn_name
    else:
        for _rn in resource_nodes:
            _rn_name = _rn.name
            # if _rn.get_all_required_parameter_names():
            #     _rn_name = f"[bold]{_rn_name}[/]"
            yield _rn_name
    # if not service:
        
    # for name, help_text in valid_completion_items:
    #     if name.startswith(incomplete) and name not in names:
    #         yield (name, help_text)


@aws_app.command('ls')
def _cli_ls_command(
        service: Optional[str] = typer.Argument(None, show_default=False,help='The AWS service name', autocompletion=_complete_service_name),
        resource_node: Optional[str] = typer.Argument(None, show_default=False, help='The AWS Resource Node', autocompletion=_complete_resource_node_name),
    ):
    """
    Lists and details AWS Services/ResourceNodes.
    TODO: Document the functions here for --help option
    """
    available_service_names = _get_available_service_node_names()
    if not service and not resource_node:
        # nothing is given
        console.print(Columns(available_service_names, equal=True, expand=True))
        return
    
    if service and not resource_node:
        # we only have service name
        
        if service not in available_service_names:
            similar_service_names = ifind_similar_names_in_list(service, available_service_names)
            if similar_service_names:
                console.print(f"[yellow]Found Similar Service Names:")
                console.print(Columns(similar_service_names, equal=True, expand=True))
                return
            else:
                raise typer.Exit(f"Invalid service name: {service}. Please pick a proper one.")
            
        service_node = ServiceNode(service, session)
        resource_nodes = service_node.get_resource_nodes()
        
        resource_node_names = []
        for _rn in resource_nodes:
            _rn_name = _rn.name
            if _rn.get_all_required_parameter_names():
                _rn_name = f"[bold]{_rn_name}[/]"
            resource_node_names.append(_rn_name)
        
        resource_node_name_as_columns =  Columns(resource_node_names, equal=True, expand=True)
        console.print(resource_node_name_as_columns)
        return
        
    elif service and resource_node:
        # we got both options filled
        service_node = ServiceNode(service, session)
        resource_nodes = service_node.get_resource_nodes()
        resource_node_names = [ _rn.name for _rn in resource_nodes]
        resource_node_obj = service_node.get_resource_node_by_name(resource_node)
        if not resource_node_obj:
            
            similar_resource_names = ifind_similar_names_in_list(resource_node, resource_node_names)
            if similar_resource_names:
                console.print(f"[yellow]Found Similar Resource Node Names:")
                console.print(Columns(similar_resource_names, equal=True, expand=True))
                return 
            else:
                raise typer.Exit(f"Invalid Resource Node name: [bold]{resource_node}[/] for Service: [bold]{service}[/].")
        operations_panel = service_node._get_operation_details_panel(resource_node_obj.name)
        console.print(operations_panel)

        return    


@aws_app.command('read')
def _cli_read_command(
        service: Optional[str] = typer.Argument(None, show_default=False,help='The AWS service name', autocompletion=_complete_service_name),
        resource_node: Optional[str] = typer.Argument(None, show_default=False, help='The AWS Resource Node', autocompletion=_complete_resource_node_name),
    ):
    available_service_names = _get_available_service_node_names()
    if not service and not resource_node:
        _cli_ls_command(service, resource_node)
        console.print(Panel(f"[bold]Please pick one of the AWS Services", title="[red][bold]ERROR"))
        return
    if service and not resource_node:
        _cli_ls_command(service, resource_node)
        console.print(Panel(f"[bold]Please pick one of the Resource Nodes from [green]{service}[/] Service", title="[red][bold]ERROR"))
        return
    elif service and resource_node:
        service_node = ServiceNode(service, session)
        service_reader = ServiceReader(service_node)
        read = service_reader.read_resource_node(resource_node)
        console.print(Pretty(read))
        # console.print(Panel(read, title=f"[green][bold]{resource_node} RESPONSE"))
        return
    
    
def run_app():
    app()
    
if __name__ == "__main__":
    # typer.run(main)
    app()
    
    




