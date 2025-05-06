from fpdf import FPDF

# PDF 클래스 생성
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "극좌표계 속도와 가속도 정리", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True, align="L")
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# 본문 내용
body_text = """
📌 극좌표계 기본 구성

극좌표계에서는 위치를 이렇게 표현해:
- R: 중심(원점)에서의 거리 → 반지름 벡터
- ϕ: 각도 (θ라고도 부름) → 회전 방향

이 좌표계에서는 단위벡터가 움직여! 그래서 속도, 가속도 표현이 복잡해져.

✅ 속도 벡터 v

수식:
v = Ṙ R̂ + Rϕ̇ ϕ̂

의미:
- Ṙ R̂ : 반지름 방향 속도 (밖으로 가거나 안으로)
- Rϕ̇ ϕ̂ : 회전 방향(접선 방향) 속도

외우는 팁:
- "반지름은 그냥 도트R" → Ṙ R̂
- "회전은 반지름 × 각속도" → Rϕ̇ ϕ̂

✅ 가속도 벡터 a

수식:
a = (R̈ - Rϕ̇²) R̂ + (2Ṙϕ̇ + Rϕ̈) ϕ̂

의미:
- R̈ R̂ : 반지름 방향의 가속도
- -Rϕ̇² R̂ : 원운동 시 생기는 구심가속도
- 2Ṙϕ̇ ϕ̂ : 코리올리 가속도
- Rϕ̈ ϕ̂ : 회전이 빨라지거나 느려지는 회전 가속도

외우는 팁:
- "반지름 방향은 → R 두 번 미분에서 빼기 원운동"
- "회전 방향은 → 속도×각속도 두 배 + 회전 가속도"

🧠 기억 정리 요약표

| 벡터 | 수식 | 기억 포인트 |
|------|------|--------------|
| v | Ṙ R̂ + Rϕ̇ ϕ̂ | 반지름 도트R, 회전 R×도트파이 |
| a | (R̈ - Rϕ̇²) R̂ + (2Ṙϕ̇ + Rϕ̈) ϕ̂ | 구심력, 코리올리, 회전 가속도 |
"""

pdf.chapter_body(body_text)

# PDF 저장
pdf.output("극좌표계_정리.pdf")

