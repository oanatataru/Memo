class Employee:
    """Base class for all employees"""

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def get_details(self):
        """Return basic details of the employee"""
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary}"

    def calculate_annual_salary(self):
        """Calculate the annual salary"""
        return self.salary * 12


class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size=0):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    def conduct_meeting(self):
        """Manager-specific method to conduct a meeting"""
        print(f"{self.name} is conducting a meeting with {self.team_size} team members.")

    def get_details(self):
        """Override to include team size"""
        return super().get_details() + f", Team Size: {self.team_size}"


class Engineer(Employee):
    def __init__(self, name, employee_id, salary, tech_stack=None):
        super().__init__(name, employee_id, salary)
        self.tech_stack = tech_stack if tech_stack else []

    def work_on_project(self, project):
        """Engineer-specific method to work on a project"""
        print(f"{self.name} is working on the project: {project} using {', '.join(self.tech_stack)}.")

    def add_skill(self, skill):
        """Add a new skill to the engineer's tech stack"""
        self.tech_stack.append(skill)
        print(f"{skill} has been added to {self.name}'s skill set.")

    def get_details(self):
        """Override to include tech stack"""
        return super().get_details() + f", Tech Stack: {', '.join(self.tech_stack)}"


class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, commission_rate=0.05):
        super().__init__(name, employee_id, salary)
        self.commission_rate = commission_rate  # Commission rate as a percentage
        self.sales_made = 0

    def make_sale(self, amount):
        """Record a sale and calculate commission"""
        commission = amount * self.commission_rate
        self.sales_made += amount
        print(f"{self.name} made a sale of ${amount}. Commission earned: ${commission}")
        return commission

    def get_details(self):
        """Override to include commission rate and sales made"""
        return super().get_details() + f", Commission Rate: {self.commission_rate * 100}%, Total Sales: ${self.sales_made}"


# Example usage
manager = Manager(name="Alice", employee_id="M001", salary=8000, team_size=10)
engineer = Engineer(name="Bob", employee_id="E002", salary=7000, tech_stack=["Python", "Django"])
salesperson = Salesperson(name="Charlie", employee_id="S003", salary=5000, commission_rate=0.10)

# Display details and use specific methods
print(manager.get_details())
manager.conduct_meeting()

print(engineer.get_details())
engineer.work_on_project("Inventory System")
engineer.add_skill("React")

print(salesperson.get_details())
salesperson.make_sale(20000)
salesperson.make_sale(5000)
