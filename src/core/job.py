import base64

class Job:
    def __init__(self, minutes, hours, days, month, week_day, location, execution, output, error) -> None:
        self.minutes = minutes
        self.hours = hours
        self.days = days
        self.month = month
        self.week_day = week_day
        self.location = location
        self.execution = execution
        self.output = output
        self.error = error
        self.__generate_id()

    
    # Each job has a unique ID that allows it to identify from the rest.
    # All its properties are used to generate an encoded ID.
    def __generate_id(self) -> str:
        self.id: base64.b64encode(
            b''+self.minutes+self.hours+self.days+self.month+self.week_day+self.location+self.execution+self.output+self.error
        )
    