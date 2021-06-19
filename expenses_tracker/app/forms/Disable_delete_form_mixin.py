class DisForMixIn():
    def __init__(self):
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True


# 'froze' - cant change,
# the string in the fields when delete
# reusable code!