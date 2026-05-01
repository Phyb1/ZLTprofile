# ZLT Company Profile - Prototype

**Live Demo**: [Add your Railway URL here]

### Problem
ZLT currently has no public website. Growers and partners cannot find basic company info, auction floor locations, or contact details online, leading to unnecessary calls to Aspindale Park.

### Solution
A responsive Django company profile site that gives ZLT a professional online presence:
- **About ZLT**: Company history, mission, and 60+ years of service
- **Services**: Auction marketing, contract farming, fast payments, market intelligence
- **Auction Floors**: Aspindale, Marondera, Karoi with contact details and hours
- **Contact**: Inquiry form and grower helpline
- **Mobile First**: Dark mode toggle, works on low-end Android devices

### Stack
Django 5.0, Python 3.12, Bootstrap 5.3, SQLite → PostgreSQL ready
Hosted on Railway with $0 free tier cost

### Impact
- Professional web presence for ZLT
- Reduces "where is the floor?" calls to staff
- Gateway for future features like live price dashboards
- Running cost: <$5/month

### Testing
```bash
python manage.py test core
