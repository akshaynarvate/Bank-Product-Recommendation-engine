import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# data importing
data = pd.read_xls('Product recommendation.xls')
df = pd.DataFrame(data=data)
df.drop(columns=['Unnamed: 0'], inplace=True)
array_df = pd.crosstab(df['Product'], df['EMAIL'])
array_df = pd.DataFrame(array_df)

# TfidfVectorizer
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(array_df)

# Cosine Similarity
similarity = cosine_similarity(feature_vectors)

df = pd.DataFrame(similarity, index=array_df.index, columns=array_df.index)




def main():
    st.title("Product Recommendation System")
    st.write("Banking Products")
    st.write(df[['Product', 'EMAIL']].head())
    st.write(" ")
    mailid = st.text_input("Enter you EMAIL")
    if st.button("Enter"):
        st.write(" ")
        if mailid in list(df["EMAIL"].unique()):
            st.write("Welcome back!")
            df.set_index(['EMAIL'], inplace=True)
            i = df[df.index == EMAIL]
            last_product = len(i['Product'].values)
            val = i['Product'].values[last_product - 1]
            st.write("your current product:", val)
            st.write("#### Products you may like ")
            col1, col2, col3 = st.columns(3)
            rec_pro = (df[val].sort_values(ascending=False))
            list1 = []
            for final_prouduct in rec_pro[1:4].index:
                list1.append(final_prouduct)
            with col1:
                st.success(list1[0])

            with col2:
                st.success(list1[1])

            with col3:
                st.success(list1[2])
        else:
            st.write("User not found!")

    st.write(" ")
    st.write("Project by Akshay Narvate")


if __name__ == "__main__":
    main()