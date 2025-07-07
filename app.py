from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')

app.secret_key = 'a_very_secret_and_complex_key_for_suman_website_2025!' # REMEMBER TO CHANGE THIS!

news_articles = [
    {
        'id': 1,
        'title': '수만, 2차전지 혁신 기술로 시장 선도',
        'date': '2025-06-20',
        'content': '수만이 최근 개발한 고효율 2차전지 제조 기술이 업계의 주목을 받고 있습니다. 이 기술은 생산성을 획기적으로 높이고 환경 부담을 줄이는 데 기여할 것으로 기대됩니다.'
    },
    {
        'id': 2,
        'title': '정밀 가공 솔루션, 스마트 팩토리 구현 앞장서',
        'date': '2025-05-15',
        'content': '당사의 스마트 정밀 가공 솔루션이 국내외 여러 기업에 성공적으로 도입되며 스마트 팩토리 전환에 기여하고 있습니다. 실시간 모니터링과 AI 기반 최적화 기능이 특징입니다.'
    },
    {
        'id': 3,
        'title': '수만, ESG 경영 강화 선언',
        'date': '2025-04-01',
        'content': '환경, 사회, 지배구조(ESG) 경영을 강화하여 지속 가능한 성장을 추구합니다. 친환경 생산 공정과 사회 공헌 활동을 확대해 나갈 예정입니다.'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/introduction.html')
def introduction():
    return render_template('introduction.html')

@app.route('/products.html')
def products():
    return render_template('products.html')

@app.route('/solutions.html')
def solutions():
    return render_template('solutions.html')

@app.route('/customer.html')
def customer():
    return render_template('customer.html')

@app.route('/news.html')
def news():
    return render_template('news.html', articles=news_articles)

@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        import time
        time.sleep(1)

        print(f"\n--- NEW CONTACT FORM SUBMISSION ---")
        print(f"Name: {name if name else 'N/A'}")
        print(f"Email: {email if email else 'N/A'}")
        print(f"Message: {message if message else 'N/A'}")
        print(f"-----------------------------------\n")

        flash('문의해주셔서 감사합니다! 최대한 빨리 답변드리겠습니다.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)