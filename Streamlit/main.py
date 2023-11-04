#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st

# Dictionary of landmarks with their details and image URLs
landmark_data = {
    "The Santa Maria": {
        "description": "The Santa Maria, known as a clumsy, complicated vessel, famously transported Christopher Columbus from Spain to the “New World” in 1492. That same year on Christmas Day, the ship ran aground. But not all was lost — another ship, the Navidad, was built with its salvaged wood.",
        "image": "https://www.boat-ed.com/blog/media/posts/26/responsive/Columbus_flagship_-Santa_Maria-_Columbus_Naval_parade_New_York_Harbor_U.S.A_from_Robert_N._Dennis_collection_of_stereoscopic_views_4-xxxl.png"
    },
    "British Luxury Liner RMS Titanic": {
        "description": "In its time, the Titanic was known as the largest ship on the sea. Considered “unsinkable,” the large luxury ship went down two hours after sideswiping an iceberg. Because of a lack of lifeboats, more than 1,500 people died in the tragedy. The ship’s wreckage was discovered in 1985 by Robert Ballard and went on to inspire one of the highest-grossing films of all time.",
        "image": "https://www.boat-ed.com/blog/media/posts/26/responsive/RMS_Titanic_3-xxxl.jpg"
    },
    "USS Constitution": {
        "description": "The USS Constitution holds the title of the longest-serving warship in history, retiring from service at 85 years old in 1882. In its time, the ship struck fear in the hearts of the British Royal Navy and gained quite the reputation as “Old Ironsides.” Even today, the ship is still intact and serves as a museum in Boston, where it takes museumgoers on a short annual cruise.",
        "image": "https://www.boat-ed.com/blog/media/posts/26/responsive/USS_Constitution_Departs-xxxl.jpg"
    },
    "HMS Victory": {
        "description": "Used by the British Royal Navy during the late 18th and early 19th century, HMS Victory is the world's oldest commissioned warship. Currently, it serves as the Flagship of the First Sea Lord, while also acting as a “living” museum in England.",
        "image": "https://www.boat-ed.com/blog/media/posts/26/responsive/HMS-Victory_-_panoramio-e1432156440746-xxxl.jpg"
    },
    "HMS Prince of Wales": {
        "description": "HMS Prince of Wales was a Royal Navy battleship that was commissioned in 1941 during World War II. Before being lost in battle in 1941, the ship performed an important role in the war. The HMS Prince of Wales was a King George V-class battleship that measured more than 220 meters in length and weighed more than 42,000 tons. It had ten 14-inch cannons, sixteen 5.25-inch guns, and numerous smaller-caliber guns. The ship also had improved radar and fire control systems.",
        "image": "https://www.havefunwithhistory.com/wp-content/uploads/2023/03/HMS-Prince-of-Wales.jpg"
    },
    "USS Enterprise": {
        "description": "The USS Enterprise is a well-known United States Navy aircraft carrier that is largely regarded as one of the most important warships in American naval history. The ship was launched in 1960 and played an important role in a number of battles, including the Vietnam War, the Gulf War, and the Afghan War.",
        "image": "https://www.havefunwithhistory.com/wp-content/uploads/2023/03/USS-Enterprise.jpg"
    },
    "USS Missouri": {
        "description": "The USS Missouri is a well-known United States Navy battleship that served in World War II and later conflicts. The ship was the last battleship built by the United States and was commissioned in 1944. The USS Missouri was an Iowa-class battleship that measured more than 270 meters in length and weighed more than 45,000 tons. It was fully armed with powerful guns and outfitted with cutting-edge radar and fire control systems.",
        "image": "https://www.havefunwithhistory.com/wp-content/uploads/2023/03/USS-Missouri.jpg"
    },
    "Queen Elizabeth 2": {
        "description": "The Queen Elizabeth 2, or QE2, was a prominent ocean liner that served from 1969 to 2008. The liner was one of the most opulent and famous of its day, and it played an important role in British maritime history.",
        "image": "https://www.havefunwithhistory.com/wp-content/uploads/2023/03/Queen-Elizabeth-2.jpg"
    },
    # Add more landmarks, their descriptions, and image URLs here...
}

st.set_page_config(page_title="Landmark Information App", layout="wide")

st.title("Explore Famous Ships")
st.markdown("---")

st.sidebar.title("Ships")
selected_landmark = st.sidebar.selectbox("Select a Ship", list(landmark_data.keys()))

st.subheader("Selected Ship Details")

if selected_landmark in landmark_data:
    st.write(f"**Landmark: {selected_landmark}**")
    st.write(f"**Description:** {landmark_data[selected_landmark]['description']}")
    st.image(landmark_data[selected_landmark]['image'], caption=f"{selected_landmark}", use_column_width=True)
else:
    st.write("No information available for this Ship.")

st.markdown("---")
st.text("Source: Various reliable sources and public domain images.")


# In[ ]:




