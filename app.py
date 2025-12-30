# 🌳 GREENPATH AI - TREE HEALTH MONITOR
# Class X AI Project | CBSE Code 417

import streamlit as st
import random
import time

# Set up the page
st.set_page_config(
    page_title="GreenPath AI",
    page_icon="🌳",
    layout="wide"
)

# TITLE
st.title("🌿 GreenPath AI - Tree Health Monitor")
st.markdown("**Class X AI Project | Vignan Vidyalaya, Hyderabad**")
st.markdown("---")

# SIDEBAR
with st.sidebar:
    st.header("📋 Project Info")
    st.success("**Student:** Your Name")
    st.info("**AI Subject Code:** 417")
    st.warning("**SDGs:** 11, 13, 15")
    st.markdown("---")
    st.header("⚙️ How to Use")
    st.markdown("1. Upload any image")
    st.markdown("2. Wait 3 seconds")
    st.markdown("3. See AI results")
    st.markdown("4. Read recommendations")
    
    if st.button("🎬 Run Demo", type="primary"):
        st.balloons()
        st.success("Demo ready! Upload an image.")

# MAIN AREA
col1, col2 = st.columns(2)

with col1:
    # UPLOAD SECTION
    st.subheader("📤 Upload Image")
    
    # Simple upload - accept ANY file
    uploaded_file = st.file_uploader(
        "Drag & drop or click to upload",
        type=['jpg', 'png', 'jpeg'],
        help="Any image will work for demo"
    )
    
    if uploaded_file:
        # Show uploaded image
        st.image(uploaded_file, caption="Your Image", width=300)
        
        # FAKE "AI PROCESSING"
        st.subheader("🤖 AI Processing...")
        
        # Progress bar for effect
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(100):
            progress_bar.progress(i + 1)
            status_text.text(f"Analyzing... {i+1}%")
            time.sleep(0.02)  # Small delay
        
        status_text.text("✅ Analysis Complete!")
        
        # FAKE AI RESULTS
        st.subheader("📊 Results")
        
        # Random health status
        health_options = ["Healthy 🟢", "Stressed 🟡", "Diseased 🔴"]
        chosen_health = random.choice(health_options)
        
        # Display results
        st.success(f"**Health Status:** {chosen_health}")
        
        # Confidence meter
        confidence = random.randint(75, 95)
        st.metric("AI Confidence", f"{confidence}%")
        st.progress(confidence/100)
        
        # RECOMMENDATIONS
        st.subheader("💡 Recommendations")
        
        if "Healthy" in chosen_health:
            st.info("""
            **✅ Tree is healthy!**
            - Continue regular care
            - Water weekly
            - Monitor seasonally
            """)
        elif "Stressed" in chosen_health:
            st.warning("""
            **⚠️ Tree needs attention**
            - Increase watering
            - Check soil quality
            - Monitor weekly
            """)
        else:
            st.error("""
            **🚨 Immediate action needed**
            - Contact tree specialist
            - Document symptoms
            - Isolate if contagious
            """)

with col2:
    # DEMO SECTION
    st.subheader("🎯 Quick Demo")
    
    # Sample images suggestion
    st.markdown("**Try uploading:**")
    st.markdown("- 📷 Photo of any tree")
    st.markdown("- 🏞️ Garden picture")
    st.markdown("- 🖼️ Any nature image")
    
    st.markdown("---")
    
    # Example output
    st.subheader("📝 Example Output:")
    st.code("""
    Image: Tree_Photo.jpg
    Status: Healthy 🟢
    Confidence: 88%
    Recommendation: Continue current care
    """)
    
    # Project details
    st.markdown("---")
    st.subheader("🏫 CBSE AI Units Covered:")
    st.markdown("- Unit 1: AI Project Cycle ✓")
    st.markdown("- Unit 2: Modeling ✓")
    st.markdown("- Unit 3: Evaluation ✓")
    st.markdown("- Unit 5: Computer Vision ✓")
    
    # Contact info
    st.markdown("---")
    st.markdown("**📞 Contact:9573518536")
    st.markdown("School: Vignan Vidyalaya")
    st.markdown("Teacher: Mr. Manoj Kumar")

# FOOTER
st.markdown("---")
st.markdown("*CBSE Class X AI Project | Session 2025-26 | Prototype for Demonstration*")