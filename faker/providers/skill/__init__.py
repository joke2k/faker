from .. import BaseProvider


class Provider(BaseProvider):
    """A skill provider that groups skills: hard skills and soft skills."""

    hard_skills = ('Analysis','Benchmarking','Big Data', 'Calculating', 'Coding', 'Configuration', 'Data Analytics',
                   'Database Design', 'Data Mining', 'Debugging','Documentation', 'Modeling', 'Needs Analysis',
                   'Statistical Analysis', 'Hardware', 'Implementation','Infrastructure', 'Maintenance', 'Networking',
                   'Network Security', 'Network Architecture', 'Programming', 'Microsoft Word', 'Linux', 'Servers', 'Security'
                   'Systems Analysis', 'Testing', 'Engineering', 'Project Planning', 'Task Management', 'Quality Control',
                   'Task Management', 'Task Delegation', 'Blogging', 'SEO', 'Web Analytics', 'Research', 'Requirements Gathering',
                   'Software Development', 'Java', 'Python', 'C#', 'Microsoft Powerpoint', 'SQL', 'Unit Testing', 'Digital Media')

    soft_skills = ('Adaptability', 'Conflict resolution','Creativity','Strong Work Ethic', 'Self Confidence',
                   'Excellent Communication','Flexibility', 'Leadership', 'Motivation', 'Patience', 'Teamwork',
                   'Negotiation', 'Visual Communication', 'Decisiveness', 'Working Well Under Pressure',
                    'Decision Making', 'Multitasking', 'Prioritization', 'Time Management', 'Accepting and integrating feedback',
                   'Collaboration', 'Empathetic', 'Planning/scheduling', 'Mentorship', 'Accountable', 'Reliable')

    all_skills = hard_skills + soft_skills

    def hard_skill(self):
        return self.random_element(self.hard_skills)

    def soft_skill(self):
        return self.random_element(self.soft_skills)

    def skill(self):
        return self.random_element(self.all_skills)
