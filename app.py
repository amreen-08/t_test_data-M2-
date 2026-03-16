import streamlit as st
import numpy as np
from scipy.stats import t
from statistics import stdev

st.title("One Sample T-Test Calculator")

# --- USER INPUTS ---

data_input = st.text_input(
    "Enter data values separated by commas",
    "52,55,49,50,58,54,53,51"
)

Mu = st.number_input("Enter Hypothesized Mean (Mu)", value=50.0)

alternative = st.selectbox(
    "Select Alternative Hypothesis",
    ["less", "greater", "two-sided"]
)

# --- FUNCTION ---
def One_Sample_T_Test_with_data(x, Mu, alternative):
    n = len(x)
    x_bar = np.mean(x)
    sd = stdev(x)
    alpha = 0.05
    df = n - 1
    sd_error = sd / np.sqrt(n)

    t_cal = (x_bar - Mu) / sd_error

    result = {}
    result["t_cal"] = t_cal

    if alternative == "less":
        p_value = t.cdf(t_cal, df)
        t_left = t.ppf(alpha, df)

        result["p_value"] = p_value
        result["critical"] = t_left
        result["decision"] = "Rejected" if t_cal < t_left else "Not Rejected"

    elif alternative == "greater":
        p_value = 1 - t.cdf(t_cal, df)
        t_right = t.ppf(1 - alpha, df)

        result["p_value"] = p_value
        result["critical"] = t_right
        result["decision"] = "Rejected" if t_cal > t_right else "Not Rejected"

    elif alternative == "two-sided":
        p_value = 2 * (1 - t.cdf(abs(t_cal), df))
        t_left = t.ppf(alpha / 2, df)
        t_right = t.ppf(1 - alpha / 2, df)

        result["p_value"] = p_value
        result["critical"] = (t_left, t_right)
        result["decision"] = "Rejected" if (t_cal < t_left or t_cal > t_right) else "Not Rejected"

    return result


# --- BUTTON ---
if st.button("Run T-Test"):

    try:
        data = [float(i) for i in data_input.split(",")]

        output = One_Sample_T_Test_with_data(data, Mu, alternative)

        st.subheader("Results")
        st.write("t_cal:", output["t_cal"])
        st.write("p_value:", output["p_value"])
        st.write("Critical Value:", output["critical"])
        st.write("Decision:", output["decision"])

    except:
        st.error("Please enter valid numeric data.")