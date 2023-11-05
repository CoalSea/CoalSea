#!/usr/bin/env python
# coding: utf-8

# In[18]:


import streamlit as st

# Dictionary of landmarks with their details and image URLs
landmark_data = {
    "Famous Ships": {
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
                    },
    "Famous Fish": {
                    "Barracuda": {
                        "description": "Barracuda are long, snakelike fish. Their mouths are full of large, needle-like teeth. The teeth fit into holes in the opposite jaw, letting them fully close their mouth. When they hunt, they either swallow prey whole or cut it in half with their sharp teeth. You can find barracuda in tropical waters around the world. They tend to hang around structures like reefs or manmade platforms like oil rigs. ",
                        "image": "https://outforia.com/wp-content/uploads/2022/09/Types-of-fish-1-09082022.avif"
                    },
                    "Snapper": {
                        "description": "Snappers are a group of fish containing over 100 species. They are large, schooling fish found in saltwater environments. They also tend to congregate around sunken structures, from reefs to dock pilings. These marine fish feed primarily on smaller, fish, crustaceans, and mollusks. ",
                        "image": "https://outforia.com/wp-content/uploads/2022/09/Types-of-fish-3-09082022.avif"
                    },
                    "Bluefish (Pomatomus saltatrix)": {
                        "description": "Bluefish get their name from their blue skin. If you cut one open, the meat has a blue tinge to it as well. They’re a widely distributed fish, found everywhere except for the Northern Pacific Ocean. In Australia, these fish are called “tailors.” ",
                        "image": "https://outforia.com/wp-content/uploads/2022/09/Types-of-fish-4-09082022.avif"
                    },
                    "Bullhead": {
                        "description": "Bullheads are a group of catfish with squared tails. There are several species of bullheads, which are closely related to channel catfish. Most of the time, bullheads don’t grow larger than 12 inches (30 cm) in length. ",
                        "image": "https://outforia.com/wp-content/uploads/2022/09/Types-of-fish-6-09082022.avif"
                    },
                    "Catfish": {
                        "description": "Catfish get their name from the barbels on their face. Those barbels look like whiskers, and like whiskers, are very sensitive. They help catfish sense vibrations in low visibility water.",
                        "image": "https://outforia.com/wp-content/uploads/2022/09/Types-of-fish-8-09082022.avif"
                    },
                    "Clownfish": {
                        "description": "Clownfish were always a popular aquarium pet, but they were made even more famous by the film Finding Nemo. Their populations have suffered because of the devastation of coral reefs and their capture for the aquarium trade. ",
                        "image": "https://outforia.com/wp-content/uploads/2022/09/Types-of-fish-11-09082022.avif"
                    },
                    "Cod": {
                        "description": "Cod is a group of coldwater fish found primarily in northern waters. They’re incredibly common and have been used for all sorts of products. The most common fish used in the English dish fish and chips is Atlantic cod. ",
                        "image": "https://www.example.com/victoria_falls_image.jpg"
                    },
                    "Lionfish": {
                        "description": "Lionfish are a beautiful and potentially painful fish to share the water with. Most lionfish have frilly fins and a tiger-stripe body pattern. They seem to float through the water with incredible grace.",
                        "image": "https://outforia.com/wp-content/uploads/2022/09/Types-of-fish-17-09082022.avif"
                    },
                    # Add more natural landmarks here...
                }
    # Add more landmarks, their descriptions, and image URLs here...
}
st.set_page_config(page_title="Nautical Information App", layout="wide")

    
st.title("Explore Famous ")
st.markdown("---")

if st.sidebar.button("Click for Stage 2"):
        st.sidebar.markdown("[Click here to go to Stage 2](https://coalsea.co/stage2/)")
st.sidebar.title("Categorys")
selected_category = st.sidebar.selectbox("Select a category", list(landmark_data.keys()))

if selected_category == "Famous Ships":
    st.subheader("Select Ship")
    selected_landmark = st.sidebar.radio("Famous Ship", list(landmark_data["Famous Ships"].keys()))
    
    st.subheader("Selected Famous Ship Details")
    if selected_landmark in landmark_data["Famous Ships"]:
        st.write(f"**Landmark: {selected_landmark}**")
        st.write(f"**Description:** {landmark_data['Famous Ships'][selected_landmark]['description']}")
        st.image(landmark_data['Famous Ships'][selected_landmark]['image'], caption=f"{selected_landmark}", use_column_width=True)
    else:
        st.write("No information available for this item.")

elif selected_category == "Famous Fish":
    st.subheader("Select Fish")
    selected_landmark = st.sidebar.radio("Famous Fish", list(landmark_data["Famous Fish"].keys()))
    
    st.subheader("Selected Famous Fish Details")
    if selected_landmark in landmark_data["Famous Fish"]:
        st.write(f"**Landmark: {selected_landmark}**")
        st.write(f"**Description:** {landmark_data['Famous Fish'][selected_landmark]['description']}")
        st.image(landmark_data['Famous Fish'][selected_landmark]['image'], caption=f"{selected_landmark}", use_column_width=True)
    else:
        st.write("No information available for this item.")

st.markdown("---")
st.text("Source: Various reliable sources and public domain images.")


# In[ ]:




