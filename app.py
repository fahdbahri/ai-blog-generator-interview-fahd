from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import os
from datetime import datetime
from seo_fetcher import fetch_seo_data
from ai_generator import generate_blog_post

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def generate():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400
    seo_data = fetch_seo_data(keyword)
    blog_content = generate_blog_post(keyword, seo_data)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"generated_posts/{keyword.replace(' ', '_')}_{timestamp}.md"
    os.makedirs("generated_posts", exist_ok=True)
    with open(filename, "w") as f:
        f.write(blog_content)
    return jsonify({
        "keyword": keyword,
        "seo_data": seo_data,
        "blog_content": blog_content,
        "filename": filename
    })

def daily_job():
    keyword = "wireless earbuds"
    seo_data = fetch_seo_data(keyword)
    blog_content = generate_blog_post(keyword, seo_data)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"generated_posts/{keyword.replace(' ', '_')}_{timestamp}.md"
    os.makedirs("generated_posts", exist_ok=True)
    with open(filename, "w") as f:
        f.write(blog_content)
    print(f"Generated daily post: {filename}")

if __name__ == "__main__":
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(daily_job, 'interval', days=1)
    # scheduler.start()
    app.run(debug=True, use_reloader=False)