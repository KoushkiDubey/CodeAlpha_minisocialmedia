



### 🚀 1-Click Local Setup (with Fixtures)

```bash
# Clone and set up
git clone https://github.com/yourusername/socialmedia-app.git
cd socialmedia-app

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Set up database with fixtures
python manage.py migrate
python manage.py loaddata users.json profiles.json posts.json comments.json

# Create admin user (optional)
python manage.py createsuperuser --username=admin --email=admin@example.com

# Run server
python manage.py runserver

🌐 Live Demo Access
A deployed version is available at:
https://web-production-bd0ab.up.railway.app


Test User Credentials
Username	Password	     Role
codealpha	CodeAlpha@123  	Superuser
testuser1	password1	    Regular user
testuser2	password2	    Regular user

### Key Features
- 🖼️ **Cloud-powered media handling** (via Cloudinary)
- 🤖 **Pre-loaded test data** (using Django fixtures)
- 💬 **Real-time interactions** (posts, comments, likes)
- 👥 **User relationship system** (following/followers)


