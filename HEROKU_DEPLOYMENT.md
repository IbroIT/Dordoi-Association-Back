# 🚀 Heroku Deployment Checklist

## ✅ Pre-deployment Tasks

### 1. Code Preparation
- [x] Update `requirements.txt` with production dependencies
- [x] Configure `settings.py` for Heroku environment variables
- [x] Add WhiteNoise for static files
- [x] Create `Procfile` for web process
- [x] Create `runtime.txt` with Python version
- [x] Add `release.py` for deployment tasks
- [x] Create health check endpoint
- [x] Update CORS settings for production

### 2. Environment Setup
- [ ] Create `.env` file from `.env.example`
- [ ] Set strong `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS` for production domain
- [ ] Set `DEBUG=False`
- [ ] Configure `CORS_ALLOWED_ORIGINS` for frontend domain

### 3. Database Configuration
- [x] Add `dj-database-url` for database URL parsing
- [x] Add `psycopg2-binary` for PostgreSQL support
- [x] Configure database settings for Heroku

## 🚀 Deployment Steps

### 1. Heroku Setup
```bash
# Create Heroku app
heroku create your-app-name

# Add PostgreSQL addon
heroku addons:create heroku-postgresql:hobby-dev

# Set environment variables
heroku config:set SECRET_KEY=your-secret-key-here
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
heroku config:set CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com
```

### 2. Deploy Code
```bash
# Commit changes
git add .
git commit -m "Prepare for Heroku deployment"

# Deploy to Heroku
git push heroku master
```

### 3. Post-deployment Setup
```bash
# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser

# Collect static files (should happen automatically via release.py)
heroku run python manage.py collectstatic --noinput
```

## 🧪 Testing

### Health Check
```bash
curl https://your-app-name.herokuapp.com/health/
# Expected: {"status": "ok", "database": "ok", ...}
```

### API Testing
```bash
# Test facts endpoint
curl "https://your-app-name.herokuapp.com/api/about-us/facts/?language=ru"

# Test partners endpoint
curl https://your-app-name.herokuapp.com/api/partners/
```

### Admin Access
- URL: `https://your-app-name.herokuapp.com/admin/`
- Use credentials created with `createsuperuser`

## 📊 Monitoring

### Logs
```bash
# View application logs
heroku logs --tail

# View release logs
heroku releases
```

### Database
```bash
# Connect to database
heroku pg:psql

# Check database info
heroku pg:info
```

## 🔧 Troubleshooting

### Common Issues

1. **Application Error (H10)**
   - Check logs: `heroku logs --tail`
   - Verify Procfile syntax
   - Check if gunicorn is in requirements.txt

2. **Database Connection Error**
   - Verify DATABASE_URL is set: `heroku config`
   - Check database addon: `heroku addons`

3. **Static Files Not Loading**
   - Verify WhiteNoise is configured
   - Check STATIC_ROOT setting
   - Run collectstatic manually

4. **CORS Errors**
   - Check CORS_ALLOWED_ORIGINS setting
   - Verify frontend domain is included

### Useful Commands

```bash
# Restart app
heroku restart

# Scale dynos
heroku ps:scale web=1

# Check app status
heroku ps

# Open app in browser
heroku open

# Run bash on Heroku
heroku run bash
```

## 📝 Production Notes

- **Security:** Never commit secrets to git
- **Backups:** Set up database backups with `heroku pg:backups`
- **Monitoring:** Consider adding New Relic or Scout APM
- **SSL:** Heroku provides automatic SSL certificates
- **Domains:** Use custom domains if needed

## 🎯 Success Criteria

- [ ] App deploys successfully without errors
- [ ] Health check returns status "ok"
- [ ] API endpoints respond correctly
- [ ] Admin panel is accessible
- [ ] Static files load properly
- [ ] Database connections work
- [ ] CORS headers are correct

## 📞 Support

If you encounter issues:
1. Check Heroku logs: `heroku logs --tail`
2. Verify environment variables: `heroku config`
3. Test locally with production settings
4. Check Heroku status page for outages