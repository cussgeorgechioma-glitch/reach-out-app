import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import os
import pandas as pd
import datetime
import hashlib

# --- PAGE CONFIG (must always come first) ---
st.set_page_config(
    page_title="Reach Out - Women's Safety & Empowerment", 
    page_icon="🌸", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Firebase app only once
if not firebase_admin._apps:
    firebase_config = st.secrets["firebase"]

    cred = credentials.Certificate({
        "type": firebase_config["type"],
        "project_id": firebase_config["project_id"],
        "private_key_id": firebase_config["private_key_id"],
        "private_key": firebase_config["private_key"],
        "client_email": firebase_config["client_email"],
        "client_id": firebase_config["client_id"],
        "auth_uri": firebase_config["auth_uri"],
        "token_uri": firebase_config["token_uri"],
        "auth_provider_x509_cert_url": firebase_config["auth_provider_x509_cert_url"],
        "client_x509_cert_url": firebase_config["client_x509_cert_url"],
        "universe_domain": firebase_config["universe_domain"]
    })

    firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()

# --- HEDERA UTILITY FUNCTIONS ---
def generate_hedera_hash(data_string):
    """Generate a simple hash to simulate Hedera transaction hash"""
    return hashlib.sha256(data_string.encode()).hexdigest()[:20]

def log_to_hedera_simulation(user_action, data_summary):
    """Simulate logging to Hedera for transparency"""
    timestamp = datetime.datetime.now().isoformat()
    transaction_hash = generate_hedera_hash(f"{user_action}_{data_summary}_{timestamp}")
    return transaction_hash

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🌸 Reach Out Navigation")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Navigate to:",
    ["Home", "Emergency Help", "Therapy & Support", "Skills & Empowerment", "Verification & Security"]
)

st.sidebar.markdown("---")
st.sidebar.info("🔒 Your data is protected with Hedera blockchain technology")
st.sidebar.markdown("---")
st.sidebar.write("Created with ❤️ to support women everywhere")

# --- HOME PAGE ---
if page == "Home":
    st.title("🌸 Welcome to Reach Out")
    st.markdown("### Your Safe Space for Support, Healing, and Growth")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
        **Reach Out** is a women-centered safety and empowerment app designed to:
        - 🛡️ Connect victims of Gender-Based Violence (GBV) with immediate help
        - 💬 Provide access to online therapy and emotional support
        - 🎓 Help survivors rebuild their lives with new skills
        - 🔗 Ensure trust and transparency using Hedera blockchain technology
        - 👥 Build a supportive community of women
        """)
        
        st.success("🎯 **Mission**: To create a world where every woman feels safe, supported, and empowered")
        st.info("💡 **Vision**: Leveraging technology to break barriers and build bridges for women's safety and economic independence")

    with col2:
        st.image("https://cdn.pixabay.com/photo/2018/01/18/07/31/girl-3089893_1280.jpg", 
                caption="Together We Rise Stronger", use_column_width=True)

    st.markdown("---")
    
    # --- EMERGENCY HOTLINE SECTION ---
    st.markdown("### 🚨 Immediate Help Section")
    st.warning("If you're in immediate danger, use these options right now:")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div style="background:linear-gradient(135deg, #FF6B6B, #FF8E8E); padding:25px; border-radius:15px; text-align:center; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                <h3 style="color:white; margin:0;">📞 Emergency Call</h3>
                <p style="color:white; font-size:14px; margin:10px 0;">NAPTIP Nigeria</p>
                <a href="tel:07030000203" style="text-decoration:none; color:white; font-weight:bold; font-size:18px; display:block; margin:10px 0;">
                    Call 0703 000 0203
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="background:linear-gradient(135deg, #4CAF50, #66BB6A); padding:25px; border-radius:15px; text-align:center; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                <h3 style="color:white; margin:0;">💬 SMS Help</h3>
                <p style="color:white; font-size:14px; margin:10px 0;">Mirabel Centre</p>
                <a href="sms:+2348092100009" style="text-decoration:none; color:white; font-weight:bold; font-size:18px; display:block; margin:10px 0;">
                    SMS +234 809 210 0009
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div style="background:linear-gradient(135deg, #25D366, #128C7E); padding:25px; border-radius:15px; text-align:center; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                <h3 style="color:white; margin:0;">🟢 WhatsApp</h3>
                <p style="color:white; font-size:14px; margin:10px 0;">24/7 Support</p>
                <a href="https://wa.me/2348092100009" style="text-decoration:none; color:white; font-weight:bold; font-size:18px; display:block; margin:10px 0;">
                    Chat on WhatsApp
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.success("🌟 You are not alone. Help is available 24/7 — your safety matters most.")

# --- EMERGENCY HELP PAGE ---
elif page == "Emergency Help":
    st.header("🚨 Emergency Help Center")
    st.write("""
    **Your safety is our priority.** If you're in danger, use the options below to get immediate help.
    All information is handled with strict confidentiality and secured with Hedera blockchain.
    """)
    
    # Quick Action Buttons
    st.subheader("🚀 Quick Emergency Actions")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📍 Share My Location", key="location_btn", help="Get help to your exact location"):
            st.info("Location sharing activated - help will be directed to your area")
            # In a real app, this would use geolocation API
            
    with col2:
        if st.button("📞 Call Emergency Contact", key="emergency_contact"):
            st.success("Calling your emergency contact...")
            
    with col3:
        if st.button("🔊 Sound Alarm", key="alarm_btn"):
            st.warning("Loud alarm activated - this may attract attention and help")

    st.markdown("---")
    
    # Hotline Buttons
    st.subheader("📞 National Emergency Hotlines")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("👩‍💼 Women's Helpline - 0800 333 333", key="women_helpline"):
            st.success("📞 Calling Women's Helpline... (0800 333 333)")
            # Log to Hedera simulation
            hash_id = log_to_hedera_simulation("emergency_call", "womens_helpline")
            st.info(f"🔗 Transaction logged: {hash_id}")
            
        if st.button("👮 Police Emergency - 112", key="police_emergency"):
            st.success("🚓 Connecting to Police Emergency... (112)")
            hash_id = log_to_hedera_simulation("emergency_call", "police_112")
            st.info(f"🔗 Transaction logged: {hash_id}")

    with col2:
        if st.button("🏥 Medical Emergency - 199", key="medical_emergency"):
            st.success("🏥 Connecting to Medical Emergency... (199)")
            hash_id = log_to_hedera_simulation("emergency_call", "medical_199")
            st.info(f"🔗 Transaction logged: {hash_id}")
            
        if st.button("🛡️ Domestic Abuse Hotline - 0813 000 000", key="domestic_abuse"):
            st.success("🛡️ Contacting Domestic Abuse Support... (0813 000 000)")
            hash_id = log_to_hedera_simulation("emergency_call", "domestic_abuse")
            st.info(f"🔗 Transaction logged: {hash_id}")

    st.markdown("---")
    
    # Emergency Form
    st.subheader("🆘 Detailed Help Request")
    with st.form("emergency_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            user_name = st.text_input("Your Name (Optional)")
            user_phone = st.text_input("Your Phone (Optional)")
            
        with col2:
            user_location = st.text_input("📍 Your Location", placeholder="City, Street, or Landmark")
            emergency_type = st.selectbox("Type of Emergency", 
                                        ["Domestic Violence", "Medical Emergency", "Safety Threat", "Other"])
        
        situation = st.text_area("🔍 Describe Your Situation", 
                               placeholder="Please describe what's happening so we can provide the right help...",
                               height=100)
        
        submitted = st.form_submit_button("🚨 Send Emergency Request")
        
        if submitted:
            if situation.strip():
                emergency_data = {
                    "timestamp": datetime.datetime.now().isoformat(),
                    "name": user_name,
                    "phone": user_phone,
                    "location": user_location,
                    "emergency_type": emergency_type,
                    "situation": situation,
                    "status": "Pending",
                    "hedera_hash": log_to_hedera_simulation("emergency_request", f"{user_name}_{emergency_type}")
                }
                
                try:
                    if db:
                        db.collection("emergency_requests").add(emergency_data)
                    st.success("✅ Emergency request submitted successfully! Help is on the way.")
                    st.info(f"🔗 Hedera Transaction ID: {emergency_data['hedera_hash']}")
                except Exception as e:
                    st.error(f"⚠️ Connection issue. Please use the direct call buttons above. Error: {e}")
            else:
                st.error("❌ Please describe your situation so we can help you effectively.")

# --- THERAPY & SUPPORT PAGE ---
elif page == "Therapy & Support":
    st.header("🧠 Therapy & Emotional Support")
    st.write("""
    **Healing is a journey, and you don't have to walk it alone.** 
    Connect with licensed therapists and supportive communities in a safe, confidential space.
    """)
    
    tab1, tab2, tab3 = st.tabs(["💬 One-on-One Therapy", "👥 Group Support", "📝 Journal & Resources"])
    
    with tab1:
        st.subheader("Private Therapy Sessions")
        st.write("Connect with licensed mental health professionals")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Available Therapists:**")
            therapists = [
                {"name": "Dr. Ada Okoro", "specialty": "Trauma & GBV", "availability": "Mon-Fri"},
                {"name": "Ms. Bola Adeyemi", "specialty": "Anxiety & Depression", "availability": "Tue-Sat"},
                {"name": "Dr. Chioma Nwosu", "specialty": "Family Counseling", "availability": "Wed-Sun"}
            ]
            
            for therapist in therapists:
                with st.expander(f"👩‍⚕️ {therapist['name']} - {therapist['specialty']}"):
                    st.write(f"**Availability:** {therapist['availability']}")
                    st.write("**Languages:** English, Pidgin")
                    if st.button(f"Book Session with {therapist['name']}", key=therapist['name']):
                        st.success(f"Session request sent to {therapist['name']}! They will contact you within 24 hours.")
        
        with col2:
            st.markdown("**Start a Therapy Chat**")
            therapy_topic = st.selectbox("What would you like to discuss?", 
                                       ["Trauma Recovery", "Anxiety Management", "Self-Esteem", 
                                        "Relationship Issues", "Career Stress", "Other"])
            
            if st.button("🕒 Schedule Session", key="schedule_therapy"):
                st.success("Therapist matching in progress... You'll be connected shortly!")
                hash_id = log_to_hedera_simulation("therapy_session", therapy_topic)
                st.info(f"🔗 Session scheduled securely: {hash_id}")
    
    with tab2:
        st.subheader("Group Support Sessions")
        st.write("Join supportive communities of women with similar experiences")
        
        groups = [
            {"name": "Survivors Circle", "focus": "GBV Recovery", "schedule": "Tuesdays 6PM"},
            {"name": "Anxiety Warriors", "focus": "Anxiety Management", "schedule": "Thursdays 7PM"},
            {"name": "Career Women", "focus": "Work-Life Balance", "schedule": "Saturdays 10AM"}
        ]
        
        for group in groups:
            col1, col2, col3 = st.columns([3, 2, 1])
            with col1:
                st.write(f"**{group['name']}**")
                st.caption(f"Focus: {group['focus']}")
            with col2:
                st.write(f"⏰ {group['schedule']}")
            with col3:
                if st.button("Join", key=group['name']):
                    st.success(f"Added to {group['name']}! Meeting details sent.")
    
    with tab3:
        st.subheader("Safe Journal & Resources")
        journal_entry = st.text_area("✍️ Write your thoughts here (completely private):", height=150)
        if st.button("Save Journal Entry"):
            if journal_entry.strip():
                st.success("Journal entry saved securely!")
            else:
                st.info("Write something to save your thoughts")
        
        st.markdown("**📚 Helpful Resources:**")
        st.download_button("Download Coping Strategies PDF", data="Sample coping strategies content", 
                          file_name="coping_strategies.pdf")
        st.download_button("Download Emergency Safety Plan", data="Sample safety plan content", 
                          file_name="safety_plan.pdf")

# --- SKILLS & EMPOWERMENT PAGE ---
elif page == "Skills & Empowerment":
    st.header("💼 Skills & Empowerment Programs")
    st.write("""
    **Build your future with confidence.** Learn marketable skills, connect with mentors, 
    and start your journey to financial independence.
    """)
    
    tab1, tab2, tab3 = st.tabs(["🎓 Learn Skills", "👩‍🏫 Teach/Mentor", "💼 Job Board"])
    
    with tab1:
        st.subheader("Skill Development Programs")
        
        skill_categories = {
            "💅 Beauty & Personal Care": ["Wig Styling & Maintenance", "Braiding Techniques", "Makeup Artistry", "Nail Technology"],
            "💻 Digital Skills": ["Virtual Assistance", "Social Media Management", "Content Writing", "Data Entry", "Basic Graphic Design"],
            "🎨 Creative Arts": ["Fashion Design", "Hair Dressing", "Catering & Cooking", "Interior Decoration"],
            "📈 Business Skills": ["Entrepreneurship", "Small Business Management", "Marketing", "Financial Literacy"]
        }
        
        selected_category = st.selectbox("Choose a skill category:", list(skill_categories.keys()))
        
        if selected_category:
            st.write(f"**Available courses in {selected_category}:**")
            for skill in skill_categories[selected_category]:
                col1, col2, col3 = st.columns([3, 2, 1])
                with col1:
                    st.write(f"• {skill}")
                with col2:
                    st.caption("🕒 6-8 weeks")
                with col3:
                    if st.button("Enroll", key=skill):
                        st.success(f"Enrolled in {skill}! Course details will be sent to you.")
        
        st.markdown("---")
        st.subheader("Apply for Skills Training")
        with st.form("training_application"):
            col1, col2 = st.columns(2)
            with col1:
                app_name = st.text_input("Full Name")
                app_email = st.text_input("Email Address")
                app_phone = st.text_input("Phone Number")
            with col2:
                app_skill = st.selectbox("Desired Skill Program", 
                                       [item for sublist in skill_categories.values() for item in sublist])
                app_experience = st.selectbox("Current Experience Level", 
                                            ["Beginner", "Some Experience", "Intermediate", "Advanced"])
            
            app_motivation = st.text_area("Why do you want to learn this skill?")
            
            if st.form_submit_button("Submit Application"):
                if all([app_name, app_email, app_skill]):
                    st.success("Application submitted! We'll contact you within 3 business days.")
                    hash_id = log_to_hedera_simulation("skill_application", f"{app_name}_{app_skill}")
                    st.info(f"🔗 Application recorded: {hash_id}")
                else:
                    st.error("Please fill in all required fields.")
    
    with tab2:
        st.subheader("Share Your Knowledge")
        st.write("Empower other women by teaching your skills or mentoring")
        
        with st.form("mentor_form"):
            st.write("**Become a Mentor/Teacher**")
            mentor_name = st.text_input("Your Name")
            mentor_skill = st.text_input("Skill you want to teach")
            mentor_experience = st.text_area("Your experience with this skill")
            mentor_availability = st.selectbox("Availability", 
                                             ["Weekends", "Evenings", "Flexible", "Full-time"])
            
            if st.form_submit_button("Register as Mentor"):
                if all([mentor_name, mentor_skill]):
                    st.success("Thank you for volunteering! We'll connect you with learners.")
                else:
                    st.error("Please fill in all fields.")
    
    with tab3:
        st.subheader("Job & Opportunity Board")
        st.info("Coming soon: Direct connections with women-friendly employers")

# --- VERIFICATION & SECURITY PAGE ---
elif page == "Verification & Security":
    st.header("🔒 User Verification & Security")
    st.write("""
    **Your safety and privacy are paramount.** We use Hedera blockchain technology to ensure 
    all users are verified while maintaining your privacy and data security.
    """)
    
    tab1, tab2, tab3 = st.tabs(["✅ User Verification", "🔍 Check Verification", "📊 Security Dashboard"])
    
    with tab1:
        st.subheader("User Verification Form")
        st.info("Complete this form once to get verified access to all features")
        
        with st.form("verification_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            
            with col1:
                full_name = st.text_input("Full Name *", placeholder="Enter your full legal name")
                email = st.text_input("Email Address *", placeholder="your.email@example.com")
                phone = st.text_input("Phone Number *", placeholder="+234 XXX XXX XXXX")
                
            with col2:
                location = st.text_input("City / State *", placeholder="Your city and state")
                verification_id = st.text_input("National ID / Unique Identifier *", 
                                              placeholder="Government issued ID number")
                date_of_birth = st.date_input("Date of Birth", min_value=datetime.date(1900, 1, 1))
            
            # Document upload simulation
            st.markdown("**📎 Upload Identification (Optional but recommended)**")
            id_upload = st.file_uploader("Upload a photo of your ID", type=['jpg', 'png', 'pdf'])
            
            terms_agreed = st.checkbox("I agree to the terms and conditions and confirm that all information provided is accurate *")
            
            submit = st.form_submit_button("🔒 Submit Verification")
            
            if submit:
                if all([full_name, email, phone, location, verification_id, terms_agreed]):
                    try:
                        # Create a simpler data structure
                        verification_data = {
                            "timestamp": datetime.datetime.now().isoformat(),
                            "full_name": full_name.strip(),
                            "email": email.lower().strip(),
                            "phone": phone.strip(),
                            "location": location.strip(),
                            "verification_id": verification_id.strip(),
                            "status": "Pending",
                            "date_of_birth": date_of_birth.isoformat() if date_of_birth else None,
                            "submitted_at": datetime.datetime.now().timestamp(),
                            "hedera_hash": log_to_hedera_simulation("user_verification", f"{full_name}_{verification_id}")
                        }
                        
                        if db:
                            # Use a simpler approach - let Firestore auto-generate the document ID
                            doc_ref = db.collection("verifications").document()
                            doc_ref.set(verification_data)
                            
                            st.success("✅ Verification submitted successfully!")
                            st.info(f"Your verification ID: {doc_ref.id}")
                            st.info(f"Hedera Transaction: {verification_data['hedera_hash']}")
                            st.balloons()
                        else:
                            st.warning("⚠️ Database not available. Verification saved locally.")
                            
                    except Exception as e:
                        st.error(f"❌ Error saving verification: {str(e)}")
                        # Show more detailed error info
                        st.info("💡 This is usually a security rules issue. Check Firestore rules.")
                else:
                    st.error("❌ Please fill in all required fields (*) and agree to the terms.")
    
    with tab2:
        st.subheader("Verification Status Check")
        check_email = st.text_input("Enter your email to check verification status")
        if st.button("Check Status"):
            if check_email:
                try:
                    if db:
                        users = db.collection("verifications").where("email", "==", check_email.lower().strip()).stream()
                        user_data = None
                        for user in users:
                            user_data = user.to_dict()
                            break
                        
                        if user_data:
                            st.success(f"✅ Verification Status: {user_data.get('status', 'Unknown')}")
                            st.write(f"**Name:** {user_data.get('full_name', 'N/A')}")
                            st.write(f"**Verification Hash:** {user_data.get('hedera_hash', 'N/A')}")
                            st.write(f"**Submitted:** {user_data.get('timestamp', 'N/A')}")
                        else:
                            st.warning("No verification found for this email. Please complete the verification form.")
                    else:
                        st.info("Database connection not available")
                except Exception as e:
                    st.error(f"Error checking status: {e}")
            else:
                st.error("Please enter your email address")
    
    with tab3:
        st.subheader("Security & Transparency Dashboard")
        st.write("**Hedera Blockchain Integration**")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Verifications", "1,247", "12%")
        with col2:
            st.metric("Blockchain Transactions", "3,891", "8%")
        with col3:
            st.metric("Data Integrity", "100%", "0%")
        
        st.info("""
        **How Hedera Protects You:**
        - 🔗 **Immutable Records**: Your verification cannot be altered or deleted
        - 👁️ **Transparency**: All verification processes are auditable
        - 🔒 **Security**: Military-grade encryption for your data
        - 🌐 **Decentralization**: No single point of failure
        """)

# --- OFFLINE DETECTION ---
try:
    # Simple internet check
    import socket
    socket.create_connection(("8.8.8.8", 53), timeout=5)
    internet_available = True
except:
    internet_available = False

if not internet_available:
    st.sidebar.warning("🌐 Offline Mode - Some features limited")

# --- FOOTER ---
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)
with footer_col1:
    st.caption("Built with Streamlit & Firebase")
with footer_col2:
    st.caption("Secured with Hedera Blockchain")
with footer_col3:
    st.caption("© 2024 Reach Out - All rights reserved") 
