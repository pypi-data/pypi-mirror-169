import importlib
import glob
from typing import List, Dict

from .Base import Base, Event
from .Script import Script
from .InfoMsgs import InfoMsgs
from .utils import pkg_path, load_from_file
from .Node import Node


class Session(Base):
    """
    The Session is the top level interface to your project. It mainly manages Scripts and registered nodes, and
    provides methods for serialization and deserialization of the project.
    """

    def __init__(
            self,
            gui: bool = False,
    ):
        Base.__init__(self)

        # events
        self.new_script_created = Event(Script)
        self.script_renamed = Event(Script)
        self.script_deleted = Event(Script)

        # ATTRIBUTES
        self.addons = {}
        self.scripts: [Script] = []
        self.nodes = set()  # list of node CLASSES
        self.invisible_nodes = set()
        self.gui: bool = gui
        self.init_data = None

        self.load_addons(pkg_path('addons/default/'))
        self.load_addons(pkg_path('addons/'))


    def load_addons(self, location: str):
        """
        Loads all addons from the given location. ``location`` can be an absolute path to any readable directory.
        """

        # discover all top-level modules in the given location
        addons = filter(lambda p: not p.endswith('__init__.py'), glob.glob(location + '/*.py'))

        for path in addons:
            # extract 'addon' object from module
            addon, = load_from_file(path, ['addon'])

            if addon is None:
                continue

            # register addon
            modname = path.split('/')[-1][:-3]
            self.addons[modname] = addon

            addon.register(self)
            setattr(Node, addon.name, addon)


    def register_nodes(self, node_classes: List):
        """Registers a list of Nodes which then become available in the flows"""

        for n in node_classes:
            self.register_node(n)


    def register_node(self, node_class):
        """Registers a single Node which then becomes available in the flows"""

        # build node class identifier
        node_class.build_identifier()

        self.nodes.add(node_class)


    def unregister_node(self, node_class):
        """Unregisters a Node which will then be removed from the available list.
        Existing instances won't be affected."""

        self.nodes.remove(node_class)


    def all_node_objects(self) -> List:
        """Returns a list of all Node objects instantiated in any flow"""

        nodes = []
        for s in self.scripts:
            for n in s.flow.nodes:
                nodes.append(n)
        return nodes


    def create_script(self, title: str = None, create_default_logs=True,
                      data: Dict = None) -> Script:
        """Creates and returns a new script.
        If data is provided the title parameter will be ignored."""

        script = Script(
            session=self, title=title, create_default_logs=create_default_logs,
            load_data=data
        )

        self.scripts.append(script)
        script.load_flow()

        self.new_script_created.emit(script)

        return script


    def rename_script(self, script: Script, title: str) -> bool:
        """Renames an existing script and returns success boolean"""

        success = False

        if self.script_title_valid(title):
            script.title = title
            success = True

        self.script_renamed.emit(script)

        return success


    def script_title_valid(self, title: str) -> bool:
        """Checks whether a considered title for a new script is valid (unique) or not"""

        if len(title) == 0:
            return False
        for s in self.scripts:
            if s.title == title:
                return False

        return True


    def delete_script(self, script: Script):
        """Removes an existing script."""

        self.scripts.remove(script)

        self.script_deleted.emit(script)


    def info_messenger(self):
        """Returns a reference to InfoMsgs to print info data"""

        return InfoMsgs


    def load(self, data: Dict) -> List[Script]:
        """Loads a project and raises an exception if required nodes are missing"""
        super().load(data)

        self.init_data = data

        # load scripts
        new_scripts = []
        for sc in data['scripts']:
            new_scripts.append(self.create_script(data=sc))

        # load addons
        for name, addon_data in data['addons'].items():
            if name in self.addons:
                self.addons[name].set_state(addon_data)
            else:
                print(f'found missing addon: {name}; attempting to load anyway')

        return new_scripts

    def serialize(self):
        """Returns the project as JSON compatible dict to be saved and loaded again using load()"""

        return self.complete_data(self.data())


    def data(self) -> dict:
        d = super().data()
        d.update({
            'scripts': [
                s.data() for s in self.scripts
            ],
            'addons': {
                name: addon.get_state() for name, addon in self.addons.items()
            }
        })
        return d
