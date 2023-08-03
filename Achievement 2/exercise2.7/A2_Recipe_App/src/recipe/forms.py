from django import forms  # import django forms

SEARCH__CHOICES = (  # specify choices as a tuple
    (
        "#1",
        "Search by Your Recipes",
    ),
    ("#2", "Search by All Recipes"),
    ("#3", "Show All Recipes"),
)


class RecipeSearchForm(forms.Form):
    search_mode = forms.ChoiceField(choices=SEARCH__CHOICES)
    search = forms.CharField(max_length=150, required=False)
