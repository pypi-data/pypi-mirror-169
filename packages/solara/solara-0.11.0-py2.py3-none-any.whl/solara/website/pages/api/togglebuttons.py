"""
# ToggleButtons

ToggleButtons are in two flavours, for single, and for multiple selections.


"""
from solara.alias import reacton, sol


@reacton.component
def Page():
    with sol.VBox() as main:
        with sol.Card("Single selection"):
            food, set_food = reacton.use_state("banana")
            sol.Markdown(f"**Selected**: {food}")
            with sol.ToggleButtonsSingle(food, on_value=set_food):
                sol.Button("Kiwi")
                sol.Button("Banana", value="banana")  # override the default value (the button label)
                sol.Button("Apple")

        with sol.Card("Multiple selections"):
            all_languages = "Python C++ Java JavaScript TypeScript BASIC".split()
            languages, set_languages = reacton.use_state([all_languages[0]])
            sol.Markdown(f"**Selected**: {languages}")
            with sol.ToggleButtonsMultiple(languages, on_value=set_languages):
                for language in all_languages:
                    sol.Button(language, value=language)

    return main
