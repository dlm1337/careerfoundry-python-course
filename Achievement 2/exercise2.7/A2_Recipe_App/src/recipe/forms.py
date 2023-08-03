from django import forms  # import django forms

SEARCH__CHOICES = (  # specify choices as a tuple
    (
        "#1",
        "Search by Your Recipes",
    ),  # when user selects "Bar chart", it is stored as "#1"
    ("#2", "Search by All Recipes"),
    ("#3", "Show All Recipes"),
)


class RecipeSearchForm(forms.Form):
    search_mode = forms.ChoiceField(choices=SEARCH__CHOICES)
    ingredient_or_recipe = forms.CharField(max_length=150, required=False)
