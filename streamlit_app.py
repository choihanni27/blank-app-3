# streamlit 라이브러리를 불러옵니다.
import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(
    page_title="Tippi - 당신의 팁을 공유하세요",
    page_icon="💡",
)

# --- 세션 상태 초기화 ---
# 'tips' 리스트가 세션 상태에 없으면 새로 생성합니다.
# 세션 상태는 사용자가 앱과 상호작용하는 동안 데이터를 기억하는 공간입니다.
if 'tips' not in st.session_state:
    st.session_state.tips = []

# --- 앱 제목 및 설명 ---
st.title("💡 Tippi")
st.markdown("다양한 주제에 대한 당신만의 팁을 공유하고 '오늘의 팁 리스트'를 만들어 보세요!")

# --- 팁 입력 폼 ---
# 'with st.form(...)'을 사용하면 여러 입력 필드를 그룹화하고
# '제출' 버튼을 눌렀을 때만 앱이 한 번에 처리하도록 할 수 있습니다.
with st.form("tip_form"):
    st.subheader("✍️ 새로운 팁 추가하기")

    # 텍스트 입력 필드 생성
    tip_study = st.text_input("학습 팁", placeholder="예: 아침에 30분 일찍 일어나기")
    tip_health = st.text_input("건강 팁", placeholder="예: 매일 물 8잔 마시기")
    tip_life = st.text_input("생활 팁", placeholder="예: 잠들기 전 내일 입을 옷 준비하기")

    # 폼 제출 버튼
    submitted = st.form_submit_button("제출")

    # 제출 버튼이 클릭되었을 때 실행될 로직
    if submitted:
        # 입력된 팁이 비어있지 않은 경우에만 세션 상태의 'tips' 리스트에 추가합니다.
        if tip_study:
            st.session_state.tips.append(f"[학습] {tip_study}")
        if tip_health:
            st.session_state.tips.append(f"[건강] {tip_health}")
        if tip_life:
            st.session_state.tips.append(f"[생활] {tip_life}")
        
        # 팁이 성공적으로 추가되었음을 사용자에게 알립니다.
        st.success("팁이 성공적으로 추가되었습니다!")

# --- 결과 출력 ---
st.subheader("📋 오늘의 팁 리스트")

# 세션 상태에 저장된 팁이 하나 이상 있는지 확인합니다.
if st.session_state.tips:
    # 번호와 함께 저장된 팁을 하나씩 화면에 출력합니다.
    for i, tip in enumerate(st.session_state.tips):
        st.info(f"{i + 1}. {tip}")
else:
    # 저장된 팁이 없으면 안내 메시지를 표시합니다.
    st.warning("아직 추가된 팁이 없습니다. 위의 양식을 통해 새로운 팁을 추가해 주세요.")