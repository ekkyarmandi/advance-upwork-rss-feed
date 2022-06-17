from datetime import datetime
import time

class Entry:

    def __init__(self, entry):

        # assign the entry into self variable
        self.hash=entry[0]
        self.title=entry[1]
        self.description=entry[2]
        self.link=entry[3]
        self.budget=entry[4]
        self.timestamp=self.calculate_time(entry[5])
        self.category=entry[6]
        self.tags=[tag.replace(" ","") for tag in entry[7].split(",")]
        self.country=entry[8]

        # refine description text
        if len(self.description) > 360:
            self.description = self.description[:360].strip() + "..."
        
        if len(self.title) > 100:
            self.title = self.title[:100].strip() + "..."

        # refine budget text
        if self.budget == "N/A":
            self.budget = "Budget: " + self.budget
        elif "-" in self.budget:
            self.budget = "Hourly Rates: " + self.budget
        else:
            self.budget = "Fixed Price: " + self.budget

    def calculate_time(self, timestamp) -> str:
        ''' Convert timestamp into string '''

        seconds = int(time.time()-timestamp)
        hours, seconds = divmod(seconds,3600)
        minutes, seconds = divmod(seconds,60)
        if hours==0:
            if minutes==1: return f"{minutes} minute ago"
            else: return f"{minutes} minutes ago"
        else:
            if hours==1 and minutes==1:
                return f"{hours} hour and {minutes} minute ago"
            else:
                if minutes==1: return f"{hours} hours and {minutes} minute ago"
                elif hours==1: return f"{hours} hour and {minutes} minutes ago"
                else: return f"{hours} hours and {minutes} minutes ago"

    def __str__(self):
        entry = dict(
            hash=self.hash,
            title=self.title,
            description=self.description,
            link=self.link,
            budget=self.budget,
            timestamp=self.timestamp,
            category=self.category,
            tags=self.tags,
            country=self.country
        )
        return str(entry)