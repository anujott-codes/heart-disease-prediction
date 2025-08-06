import streamlit as st
import pandas as pd
import joblib
import time

# Configure page
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin: -1rem -1rem 2rem -1rem;
        border-radius: 0 0 20px 20px;
    }
    
    .section-header {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border: 1px solid #e9ecef;
        text-align: center;
    }
    
    .risk-high {
        background: linear-gradient(90deg, #ff6b6b, #ee5a52);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        font-size: 1.2rem;
    }
    
    .risk-low {
        background: linear-gradient(90deg, #51cf66, #40c057);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        font-size: 1.2rem;
    }
    
    .info-box {
        background: #e3f2fd;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #2196f3;
        margin: 1rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .sidebar-content {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Load models (you'll need to uncomment these when you have the actual files)
# model = joblib.load("log_reg.pkl")
# scaler = joblib.load("scaler.pkl")
# expected_columns = joblib.load("columns.pkl")

# Header
st.markdown("""
<div class="main-header">
    <h1>❤️ Heart Disease Risk Assessment</h1>
    <p>Advanced AI-powered cardiovascular health evaluation</p>
</div>
""", unsafe_allow_html=True)

# Create main layout
col1, col2 = st.columns([2, 1])

with col1:
    # Demographics Section
    st.markdown("""
    <div class="section-header">
        <h3>👤 Demographics</h3>
        <p>Basic demographic information</p>
    </div>
    """, unsafe_allow_html=True)
    
    demo_col1, demo_col2 = st.columns(2)
    
    with demo_col1:
        st.markdown("**Age**")
        st.caption('Age should be greater than or equal to 18')
        age = st.slider("", 18, 100, 40, key="age")
        st.markdown(f"<div class='metric-card'><strong>{age} years old</strong></div>", unsafe_allow_html=True)
    
    with demo_col2:
        st.markdown("**Gender**")
        sex = st.selectbox("", ['Select Gender', 'M', 'F'], key="sex")
        if sex != 'Select Gender':
            gender_display = "Male" if sex == 'M' else "Female"
            st.markdown(f"<div class='metric-card'><strong>{gender_display}</strong></div>", unsafe_allow_html=True)

    # Vital Signs Section
    st.markdown("""
    <div class="section-header">
        <h3>🩺 Vital Signs & Lab Results</h3>
        <p>Blood pressure, cholesterol, and other measurements</p>
    </div>
    """, unsafe_allow_html=True)
    
    vital_col1, vital_col2 = st.columns(2)
    
    with vital_col1:
        st.markdown("**Resting Blood Pressure**")
        resting_bp = st.slider("mm Hg", 40, 200, 80, key="bp")
        
        st.markdown("**Cholesterol Level**")
        cholesterol = st.slider("mg/dL", 100, 650, 200, key="chol")
        
        # Display current values
        bp_status = "Normal" if resting_bp < 120 else "Elevated" if resting_bp < 140 else "High"
        chol_status = "Normal" if cholesterol < 200 else "Borderline" if cholesterol < 240 else "High"
        
        st.markdown(f"""
        <div class='metric-card'>
            <strong>{resting_bp} mm Hg</strong><br>
            <small>{bp_status}</small>
        </div>
        """, unsafe_allow_html=True)
    
    with vital_col2:
        st.markdown("**Maximum Heart Rate**")
        max_hr = st.slider("bpm", 60, 220, 150, key="hr")
        
        st.markdown("**Oldpeak (ST Depression)**")
        old_peak = st.slider("", 0.0, 6.0, 1.0, key="oldpeak")
        
        # Display current values
        st.markdown(f"""
        <div class='metric-card'>
            <strong>{max_hr} bpm</strong><br>
            <small>Max Heart Rate</small>
        </div>
        """, unsafe_allow_html=True)

    # Clinical Parameters Section
    st.markdown("""
    <div class="section-header">
        <h3>🔬 Clinical Parameters</h3>
        <p>Symptoms and diagnostic test results</p>
    </div>
    """, unsafe_allow_html=True)
    
    clinical_col1, clinical_col2 = st.columns(2)
    
    with clinical_col1:
        st.markdown("**Chest Pain Type**")
        chest_pain_options = {
            'Select Type': '',
            'Atypical Angina': 'ATA',
            'Non-Anginal Pain': 'NAP', 
            'Typical Angina': 'TA',
            'Asymptomatic': 'ASY'
        }
        chest_pain_display = st.selectbox("", list(chest_pain_options.keys()), key="chest_pain")
        chest_pain = chest_pain_options[chest_pain_display]
        
        st.markdown("**ST Slope**")
        st_slope_options = {
            'Select Slope': '',
            'Upsloping': 'Up',
            'Downsloping': 'Down',
            'Flat': 'Flat'
        }
        st_slope_display = st.selectbox("", list(st_slope_options.keys()), key="st_slope")
        st_slope = st_slope_options[st_slope_display]
    
    with clinical_col2:
        st.markdown("**Fasting Blood Sugar ≥ 120 mg/dL**")
        fasting_bs = st.radio("", ['Yes', 'No'], key="fasting", horizontal=True)
        
        st.markdown("**Resting ECG**")
        ecg_options = {
            'Normal': 'Normal',
            'ST-T Wave Abnormality': 'ST',
            'Left Ventricular Hypertrophy': 'LVH'
        }
        resting_ecg_display = st.radio("", list(ecg_options.keys()), key="ecg")
        resting_ecg = ecg_options[resting_ecg_display]
        
        st.markdown("**Exercise Induced Angina**")
        excercise_angina = st.radio("", ['Y', 'N'], key="angina", horizontal=True)
        st.caption("Y: Yes, N: No")

    # Prediction Button
    st.markdown("<br>", unsafe_allow_html=True)
    predict_col1, predict_col2, predict_col3 = st.columns([1, 2, 1])
    
    with predict_col2:
        if st.button('🔍 Analyze Heart Disease Risk', use_container_width=True):
            # Validate inputs
            if (sex == 'Select Gender' or chest_pain == '' or st_slope == '' or 
                not fasting_bs or not resting_ecg or not excercise_angina):
                st.error("⚠️ Please fill in all required fields")
            else:
                # Show loading
                with st.spinner('Analyzing your health data...'):
                    time.sleep(2)  # Simulate processing time
                    
                    # Your original prediction logic
                    raw_input = {
                        'Age': age,
                        'RestingBP': resting_bp,
                        'Cholesterol': cholesterol,
                        'FastingBS': 1 if fasting_bs == 'Yes' else 0,
                        'MaxHR': max_hr,
                        'Oldpeak': old_peak,
                        'Sex_' + sex: 1,
                        'ChestPainType_' + chest_pain: 1,
                        'RestingECG_' + resting_ecg: 1,
                        'ExcerciseAngina_' + excercise_angina: 1,
                        'ST_slope_' + st_slope: 1
                    }
                    
                    # Mock prediction (replace with your actual model)
                    # input_df = pd.DataFrame([raw_input])
                    # for col in expected_columns:
                    #     if col not in input_df.columns:
                    #         input_df[col] = 0
                    # input_df = input_df[expected_columns]
                    # cols_to_scale = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
                    # input_df.loc[:,cols_to_scale] = scaler.transform(input_df.loc[:,cols_to_scale])
                    # prediction = model.predict(input_df)[0]
                    
                    # Mock prediction for demo
                    risk_factors = sum([
                        age > 60,
                        resting_bp > 140,
                        cholesterol > 240,
                        fasting_bs == 'Yes',
                        excercise_angina == 'Y',
                        old_peak > 2.0
                    ])
                    prediction = 1 if risk_factors >= 3 else 0
                    
                    # Store prediction in session state
                    st.session_state.prediction = prediction
                    st.session_state.risk_factors = risk_factors

# Right sidebar for results
with col2:
    st.markdown("""
    <div class="section-header">
        <h3>📊 Risk Assessment Results</h3>
    </div>
    """, unsafe_allow_html=True)
    
    if 'prediction' not in st.session_state:
        st.markdown("""
        <div class="info-box">
            <h4>🏥 Waiting for Analysis</h4>
            <p>Complete the form on the left and click "Analyze Heart Disease Risk" to see your personalized assessment.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Show some health tips while waiting
        st.markdown("""
        <div class="sidebar-content">
            <h4>💡 Heart Health Tips</h4>
            <ul>
                <li>Regular exercise (150 min/week)</li>
                <li>Maintain healthy weight</li>
                <li>Limit sodium intake</li>
                <li>Don't smoke</li>
                <li>Manage stress levels</li>
                <li>Get adequate sleep</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    else:
        prediction = st.session_state.prediction
        risk_factors = st.session_state.risk_factors
        
        if prediction == 1:
            st.markdown("""
            <div class="risk-high">
                ⚠️ HIGH RISK OF HEART DISEASE
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="info-box">
                <h4>⚠️ Important Notice</h4>
                <p>Based on the provided information, our AI model indicates an elevated risk for heart disease.</p>
                <p><strong>Risk Factors Identified:</strong> {risk_factors}/6</p>
            </div>
            """, unsafe_allow_html=True)
            
        else:
            st.markdown("""
            <div class="risk-low">
                ✅ LOW RISK OF HEART DISEASE
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="info-box">
                <h4>✅ Good News!</h4>
                <p>Based on the provided information, our AI model indicates a lower risk for heart disease.</p>
                <p><strong>Risk Factors Identified:</strong> {risk_factors}/6</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Risk factor breakdown
        st.markdown("**Risk Factor Analysis:**")
        
        factors = [
            ("Age > 60", age > 60),
            ("High BP", resting_bp > 140),
            ("High Cholesterol", cholesterol > 240),
            ("High Fasting BS", fasting_bs == 'Yes'),
            ("Exercise Angina", excercise_angina == 'Y'),
            ("High Oldpeak", old_peak > 2.0)
        ]
        
        for factor, present in factors:
            status = "🔴" if present else "🟢"
            st.write(f"{status} {factor}")
        
        # Medical disclaimer
        st.markdown("""
        <div class="info-box">
            <h4>⚕️ Medical Disclaimer</h4>
            <p><small>This prediction is for informational purposes only and should not replace professional medical advice. Please consult with a healthcare provider for proper diagnosis and treatment.</small></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Reset button
        if st.button('🔄 New Assessment', use_container_width=True):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.rerun()

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666; border-top: 1px solid #eee; margin-top: 2rem;">
    <p>❤️ Heart Disease Prediction System | Powered by AI & Machine Learning</p>
    <p><small>Always consult with healthcare professionals for medical decisions</small></p>
</div>
""", unsafe_allow_html=True)
