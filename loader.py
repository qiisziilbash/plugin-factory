import importlib


class PluginInterface:
    """Represents a plugin interface. A plugin has a single register function."""

    @staticmethod
    def register() -> None:
        """Register the necessary items in the game character factory."""


def import_plugin(name: str) -> PluginInterface:
    return importlib.import_module(f"plugins.{name}")


def load_plugins(plugin_names: list[str]) -> None:
    for plugin_name in plugin_names:
        plugin = import_plugin(plugin_name)
        plugin.register()
