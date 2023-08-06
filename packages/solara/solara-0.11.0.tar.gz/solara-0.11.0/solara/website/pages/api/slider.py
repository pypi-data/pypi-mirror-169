"""
# Slider

To support proper typechecks, we have multiple slider (all wrapping the ipyvuetify slider).
"""
import datetime

from solara.alias import reacton, sol


@reacton.component
def Page():
    with sol.VBox() as main:
        with sol.Card("Integers"):
            int_value, set_int_value = reacton.use_state(42)
            sol.IntSlider("Some integer", value=int_value, min=-10, max=120, on_value=set_int_value)
            sol.Markdown(f"**Int value**: {int_value}")

        with sol.Card("Floats"):
            float_value, set_float_value = reacton.use_state(42.4)
            sol.FloatSlider("Some float", value=float_value, min=-10, max=120, on_value=set_float_value)
            sol.Markdown(f"**Float value**: {float_value}")

        with sol.Card("Values"):
            values = "Python C++ Java JavaScript TypeScript BASIC".split()
            value, set_value = reacton.use_state(values[0])
            sol.ValueSlider("Language", value, values=values, on_value=set_value)
            sol.Markdown(f"**Value**: {value}")

        with sol.Card("Dates"):
            date, set_date = reacton.use_state(datetime.date(1981, 7, 28))
            sol.DateSlider("Some date", value=date, on_value=set_date)
            sol.Markdown(f"**Date**: {date.strftime('%Y-%b-%d')}")

    return main
