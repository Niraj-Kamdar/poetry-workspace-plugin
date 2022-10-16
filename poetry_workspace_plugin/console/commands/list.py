from poetry.console.commands.command import Command

from poetry_workspace_plugin.helpers import get_workspaces_table


class WorkspaceListCommand(Command):
    name = "workspace list"
    description = "Lists workspaces tracked in current project."

    def handle(self) -> int:
        workspaces = get_workspaces_table(self.poetry.file.read())
        if not workspaces:
            return 0
        table = self.table(style="compact")
        table.add_rows([[f"<c1>{name}</>", path] for name, path in workspaces.items()])
        table.render()
        return 0
