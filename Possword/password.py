import streamlit as st
import re

st.set_page_config(page_title="Password Strength checker", page_icon="🔐", layout="centered")
    
st.markdown("""
<style>
   .stSidebar {
    background-color:black;
   }
 .stSidebar{
            color: white;
  }
.sidebar-text {
            color: white;
 }
            
</style

""" , unsafe_allow_html=True)


st.title("🔐 Password Strength Checker")

st.sidebar.image('./pic.png')
st.sidebar.markdown('<hr style="height: 1px; background-color: white; margin-top:0px"/>', unsafe_allow_html=True)
st.sidebar.header("💪 Strong Password Criteria:👇")
st.sidebar.markdown('<p class="sidebar-text">📏 Minimum 8 characters</p>', unsafe_allow_html=True)
st.sidebar.markdown('<p class="sidebar-text">🔠 Upper and lower case letters (A-Z, a-z)</p>', unsafe_allow_html=True)
st.sidebar.markdown('<p class="sidebar-text">🔢 At least one number (0-9)</p>', unsafe_allow_html=True)
st.sidebar.markdown('<p class="sidebar-text">🔣 At least one special character (!@#$%^&*)</p>', unsafe_allow_html=True)



def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("⚠️ Password should be at least 8 characters long.")
    
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("⚠️ Include both uppercase and lowercase letters.")
    
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("⚠️ Add at least one digit (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append(" ⚠️Include at least one special character (!@#$%^&*).")
    
    if score == 4:
        feedback.append("✅ Your password is strong!")
    return score, feedback
    

def main():
   
    st.info("Enter a password to check its strength and get improvement suggestions. 💭")
    
    password = st.text_input("Enter your password:", type="password" , placeholder="Enter your password here...")
    
    if st.button("Check Password Strength"):
        if password:
            score, feedback = check_password_strength(password)
            
            st.write("### Password Strength:")
            
            progress_color = "#dc3545"  # Default red for weak
            progress_value = (score / 4) * 100
            
            if score == 4:
                progress_color = "#28a745"  # Green for strong
            elif score == 3:
                progress_color = "#ffc107"  # Yellow for moderate
            
            st.markdown(
                f'<div style="width: 100%; background: #ddd; border-radius: 8px;">'
                f'<div style="width: {progress_value}%; background: {progress_color}; height: 10px; border-radius: 8px;"></div>'
                f'</div>',
                unsafe_allow_html=True
            )
            
            if score <= 2:
                st.error(" Weak Password! Improve it using the suggestions below.")
            elif score == 3:
                st.warning(" Moderate Password! Consider strengthening it.")
            else:
                st.success("✅ Strong Password! Well done.")
            
            st.write("### Suggestions:")
            for tip in feedback:
                st.write(f"- {tip}")
        else:st.warning("Enter a password to check its strength.")

if __name__ == "__main__":
    main()

st.markdown("---")
st.markdown("""<h6 style="text-align: center; color: #333; ">Developed by || Rimsha Sultan</h3>""", unsafe_allow_html=True)
