from django.contrib.auth.models import  AbstractUser 
from django.db import models


class User(AbstractUser):
    USER_TYPES = [
        ('admin', 'Admin'),
        ('karfarma', 'Karfarma'),
        ('karjo', 'Karjo'),
    ]
    #role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    user_type = models.CharField(max_length=7, choices=USER_TYPES)

    # شماره موبایل کاربر که منحصر به فرد است و می‌تونیم ازش برای ورود به سیستم هم استفاده کنیم
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)

    # تعریف متد __str__ برای نمایش خوانا‌تر از مدل در Django Admin یا جاهای دیگه
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"

class OrganizationProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'karfarma'})
    karfarma = models.OneToOneField( 'KarfarmaProfile',on_delete=models.CASCADE, related_name='organizationprofile')
    # مشخصات سازمان
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    website_address = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    
    # توضیحات و موقعیت جغرافیایی
    about = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=100)  # استان محل سازمان

    # حوزه فعالیت سازمان
    activity_area = models.TextField(blank=True, null=True)  # حوزه فعالیت

    # تعداد کارمندان و سال تأسیس
    number_of_employees = models.IntegerField(blank=True, null=True)  # تعداد کارمندان
    year_of_establishment = models.IntegerField(blank=True, null=True)  # سال تأسیس

    # تصاویر و ویدیوها
    profile_background_image = models.ImageField(upload_to='backgrounds/', blank=True, null=True)  # تصویر پس‌زمینه پروفایل
    media = models.FileField(upload_to='media/', blank=True, null=True)  # تصاویر یا ویدیوهای سازمان

    created_at = models.DateTimeField(auto_now_add=True) # زمان ثبت‌نام
    
    def __str__(self):
        return self(all)

class JobPosting(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]


    title = models.CharField(max_length=255)  # عنوان آگهی شغلی
    description = models.TextField()  # توضیحات مربوط به شغل
    location = models.CharField(max_length=255)  # محل کار
    posted_date = models.DateField(auto_now_add=True)  # تاریخ انتشار آگهی  
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)  # جنسیت
    type_of_employment = models.CharField(max_length=100)  # نوع استخدام
    military_service_status = models.CharField(max_length=100)  # وضعیت خدمت نظام وظیفه
    salary = models.CharField(max_length=100)  # حقوق
    state = models.CharField(max_length=100)  # استان
    city = models.CharField(max_length=100)  # شهر
    minimum_educational_qualification = models.CharField(max_length=100)  # حداقل مدرک تحصیلی
    #address = models.CharField(max_length=255)  # آدرس
    job_skill = models.CharField(max_length=100)  # مهارت شغلی
    level_of_proficiency = models.CharField(max_length=100)  # سطح تسلط
    benefits_and_facilities = models.TextField()  # مزایا و تسهیلات

    def __str__(self):
        return self.title

class Product(models.Model):
    # ارتباط با کارفرما (Karfarma)
    karfarma = models.ForeignKey('KarfarmaProfile', on_delete=models.CASCADE, related_name='products')

    # اطلاعات محصول
    name = models.CharField(max_length=255)  # نام محصول
    description = models.TextField(blank=True, null=True)  # توضیحات محصول
    price = models.IntegerField()  # قیمت محصول
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # تصویر محصول

    # تاریخ‌های مرتبط
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد محصول
    updated_at = models.DateTimeField(auto_now=True)  # تاریخ آخرین بروزرسانی

    def __str__(self):
        return self.name

class KarjoProfile(models.Model):
    # فیلدهای اضافی برای کارجو
    full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    

    def __str__(self):
        return self.full_name

class Resume(models.Model):

    karjo = models.ForeignKey('karjoProfile', on_delete=models.CASCADE, related_name='resumes')  # کارجو

    
    #job_title = models.CharField(max_length=255, verbose_name="عنوان شغلی")  # عنوان شغلی
    about = models.TextField(verbose_name="درباره من")  # توضیح کوتاه درباره خود
    #experience = models.TextField(verbose_name="تجربه کاری")  # تجربه کاری
    #projects = models.TextField(verbose_name="پروژه‌ها")  # پروژه‌ها 
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="تاریخ تولد")  # تاریخ تولد
    marital_status = models.CharField(max_length=20, verbose_name="وضعیت تاهل")  # وضعیت تاهل
    gender = models.CharField(max_length=10, verbose_name="جنسیت")  # جنسیت
    city = models.CharField(max_length=100, verbose_name="شهر")  # شهر
    state = models.CharField(max_length=100, verbose_name="استان")  # استان
    address = models.TextField(verbose_name="آدرس")  # آدرس
    educational_level = models.CharField(max_length=100, verbose_name="سطح تحصیلات")  # سطح تحصیلات
    field_of_study = models.CharField(max_length=100, verbose_name="رشته تحصیلی")  # رشته تحصیلی
    university_name = models.CharField(max_length=255, verbose_name="نام دانشگاه/مؤسسه")  # نام دانشگاه/مؤسسه
    education_start_date = models.DateField(null=True, blank=True, verbose_name="تاریخ شروع تحصیلات")  # تاریخ شروع تحصیلات
    education_end_date = models.DateField(null=True, blank=True, verbose_name="تاریخ پایان تحصیلات")  # تاریخ پایان تحصیلات
    organization_name = models.CharField(max_length=255, verbose_name="نام سازمان")  # نام سازمان
    job_start_date = models.DateField(null=True, blank=True, verbose_name="تاریخ شروع کار")  # تاریخ شروع کار
    job_end_date = models.DateField(null=True, blank=True, verbose_name="تاریخ پایان کار")  # تاریخ پایان کار
    skill = models.CharField(max_length=100, verbose_name="مهارت")  # مهارت
    proficiency_level = models.CharField(max_length=100, verbose_name="سطح تسلط")  # سطح تسلط
    instagram_address = models.URLField(null=True, blank=True, verbose_name="آدرس اینستاگرام")  # آدرس اینستاگرام
    linkedin_address = models.URLField(null=True, blank=True, verbose_name="آدرس لینکدین")  # آدرس لینکدین
    github_address = models.URLField(null=True, blank=True, verbose_name="آدرس گیت‌هاب")  # آدرس گیت‌هاب
    resume_attachment = models.FileField(upload_to='resumes/', null=True, blank=True, verbose_name="بارگذاری رزومه")  # بارگذاری رزومه


    def __str__(self):
        return f"Resume of {self.full_name}"
        
class Ticket(models.Model):
    pass


