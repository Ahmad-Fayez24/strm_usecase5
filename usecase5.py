import streamlit as st

# Title and Introduction
st.title("Exploring the Kingdom’s Job Market: A Deep Dive into Opportunities and Trends")
st.write("""
In this analysis, we’re shedding light on the job market across the Kingdom of Saudi Arabia, unveiling insights into job distribution by region, gender preferences, experience requirements, and salary expectations for fresh graduates.
""")

# Step 1: Regional Distribution of Job Postings
st.header("1. Regional Distribution of Job Postings")
st.write("""
Starting with the geographical spread, the analysis reveals that certain regions hold a larger share of job opportunities than others. 
**A significant portion of job openings are concentrated in Riyadh**, underscoring the city’s role as a central business hub. Other regions, like the Eastern Province, also show strong numbers but do not match Riyadh’s volume.
""")

# Display pie chart as an image
st.image("out.png", caption="Proportion of Job Postings by Region")

# Step 2: Gender Preferences in Job Postings
st.header("2. Gender Preferences in Job Postings")
st.write("""
The data analysis uncovered an inclusive trend in terms of gender preferences. Most job postings appear to be open to both men and women, with few positions specifically targeting male candidates. 
This inclusivity in the job market aligns with ongoing shifts towards greater workforce diversity in the Kingdom, especially in sectors that traditionally favored one gender over the other.
""")

# Display gender preference bar chart as an image
st.image("output2.png", caption="Gender Preference in Job Postings")

# Step 3: Salary Expectations for Fresh Graduates
st.header("3. Salary Expectations for Fresh Graduates")
st.write("""
One key question for new entrants into the workforce is salary expectations. We focused on postings that required no prior experience, representing positions available to fresh graduates. 
The analysis revealed that **salary ranges for fresh graduates tend to cluster around 4,000 to 5,000 SAR**, with only a few outliers.
""")

# Display salary range box plot as an image
st.image("output3.png", caption="Salary Range for Fresh Graduates")

# Step 4: Opportunities for Fresh Graduates vs. Experienced Professionals
st.header("4. Opportunities for Fresh Graduates vs. Experienced Professionals")
st.write("""
Finally, we examined the experience requirements to understand if the job market is more favorable for fresh graduates or if there is room for fresh graduates as well. 
The findings suggest that **a notable portion of positions are open to fresh graduates**, yet the majority lean toward candidates with prior experience.
""")

# Display job opportunities bar chart as an image
st.image("output4.png", caption="Job Opportunities for Fresh Graduates vs. Experienced Candidates")

# Conclusion
st.subheader("Conclusion")
st.write("""
This analysis paints a comprehensive picture of the job market in Saudi Arabia. Job opportunities are largely concentrated in the central regions, particularly Riyadh, with an inclusive approach to gender in many postings. 
Fresh graduates can anticipate salaries within a specific range as they step into roles that don’t require prior experience, though experienced candidates remain in high demand.
Together, these insights reflect a dynamic job market, one that aligns with Saudi Arabia's broader Vision 2030 goals of economic diversification and workforce inclusivity.
""")
