import streamlit as st
import random
from datetime import datetime

st.title("🎱 로또 번호 자동 생성기")
st.caption("버튼을 누르면 1~45 사이의 중복 없는 번호 6개짜리 세트를 5개 만들어줍니다.")

st.markdown("---")

# 동행복권 공식 기준 색상 공 매핑
def get_ball_emoji(num: int) -> str:
    if num <= 10:
        return "🟡"  # 1~10: 노랑
    elif num <= 20:
        return "🔵"  # 11~20: 파랑
    elif num <= 30:
        return "🔴"  # 21~30: 빨강
    elif num <= 40:
        return "🔘"  # 31~40: 회색
    else:
        return "🟢"  # 41~45: 초록

def lotto_one_set() -> list:
    """1~45 에서 중복 없이 번호 6개 뽑아 정렬된 리스트로 반환"""
    number = set()
    while len(number) < 6:
        number.add(random.randint(1, 45))
    return sorted(number)

if st.button("5세트 번호 생성하기", key="lotto_generate_btn"):
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.write(f"생성된 시각 : **{now_str}**")

    for set_index in range(1, 6):
        lotto_num = lotto_one_set()
        # 번호 앞에 공식 색상 공 이모지 매핑 (예: 🟡 3  🔵 15  🔴 22 ...)
        formatted_nums = "  ".join([f"{get_ball_emoji(n)} {n}" for n in lotto_num])
        st.write(f"**{set_index}세트** : {formatted_nums}")