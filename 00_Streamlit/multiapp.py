import streamlit as st

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        app_state = st.experimental_get_query_params()

        # fetch the first item in each query string as we don't have multiple values for each query string key in this example
        app_state = {
            k: v[0] if isinstance(v, list) else v for k, v in app_state.items()
        }  

        titles = [a["title"] for a in self.apps]
        functions = [a["function"] for a in self.apps]
        default_radio = titles.index(app_state["page"]) if "page" in app_state else 0

        st.sidebar.title(":rain_cloud: Projet PyAusRainfall :umbrella_with_rain_drops:")

        title = st.sidebar.radio("Menu", titles, index=default_radio, key="radio")

        app_state["page"] = st.session_state.radio

        st.experimental_set_query_params(**st.session_state.to_dict())
        functions[titles.index(title)]()
