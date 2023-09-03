from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
import streamlit as st
import plotly.express as px


class LanguageProcessing:
    def __init__(
        self,
        input_lst,
        category: str = "Category",
        value: str = "Value",
        index: str = "Index",
    ):
        self._analyzer = SentimentIntensityAnalyzer()
        self._input_lst = input_lst
        self._category = category
        self._value = value
        self._index = index
        self._input_analyzer = {
            self._category: [],
            self._value: [],
            self._index: [],
        }
        self._input_analyzer_score()

    def _input_analyzer_score(self):
        for index, text in enumerate(self._input_lst):
            self._input_analyzer[self._category].append("Positivity")
            self._input_analyzer[self._category].append("Negativity")
            self._input_analyzer[self._value].append(
                self._analyzer.polarity_scores(text)["pos"]
            )
            self._input_analyzer[self._value].append(
                self._analyzer.polarity_scores(text)["neg"]
            )
            self._input_analyzer[self._index].append(index + 1)
            self._input_analyzer[self._index].append(index + 1)

    def graph_representation(self, title):
        df = pd.DataFrame(self._input_analyzer)
        line_chart = px.line(
            df, x=self._index, y=self._value, color=self._category, title=title
        )
        st.plotly_chart(line_chart)

    def set_index(self, dates):
        self._input_analyzer[self._index] = dates
