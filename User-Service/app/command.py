import abc

class Command(metaclass=abc.ABCMeta):
    """
    The command interface that declares a method (execute) for a particular
    action.
    """
    @abc.abstractmethod
    def execute(self):
        pass

class PremiumMembership:
    """
    The receiver class, which holds the specifc method to be called to
    perform the specific action.
    This will be called by the Invoker object.
    """

    def premium_member(self):
        print("Premium Membership user logged in")


class NonPremium_Membership:
    """
    The receiver class, which holds the specific method to be called.
    This will be called by the Invoker object.
    """

    def nonpremium_member(self):
         print("Non-Premium Membership user logged in")

#Premium command interface
class PremiumCommand(Command):
    """
    A concrete / specific Command class, implementing exectue()
    which calls a specific or an appropriate action of a method
    from a Receiver class.
    
    """
    def __init__(self, premium_member: PremiumMembership):
        self._premium = premium_member

    def execute(self):
        self._premium.premium_member()


class NonPremiumCommand(Command):
    def __init__(self, nonpremium_member: NonPremium_Membership):
        self._nonpremium = nonpremium_member

    def execute(self):
        self._nonpremium.nonpremium_member()

class MembershipInvoker:
    """
    Has a reference to the Command, and can execute the method.
    Notice how the command.execute() is never directly called,
    but always through the invoker.
    The action invoked is decoupled from the action performed
    by the Receiver.
    The Invoker (self) invokes a Command (),
    and the Command executes the appropriate action (command.execute())
    """

    def __init__(self, command: Command):
        self._command = command
        self._command_list = []  # type: List[Command]

    def set_command(self, command: Command):
        self.command = command

    def get_command(self):
        print(self.command.__class__.__name__)

    def add_command_to_list(self, command: Command):
        self._command_list.append(command)

    def execute_commands(self):
        """
        Execute all the saved commands, then empty the list.
        """
        for cmd in self._command_list:
            cmd.execute()

        self._command_list.clear()

    def invoke(self):
        self._command.execute()