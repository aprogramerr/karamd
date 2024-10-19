from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# class admin(AbstractUser):
#     pass

class Karfarma(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # ...

class Organization(models.Model):
    """
    اطلاعات سازمان که کارفرما وارد میکند
    """
    ACTIVITY_CHOICES = [
        ('digital_marketing', 'دیجیتال مارکتینگ'),
        ('graphic_animation', 'طراحی گرافیک/انیمیشن'),
        ('ui_design', 'طراحی رابط کاربری'),
        ('ux_design', 'طراحی تجربه کاربری'),
        ('seo', 'سئو'),
        ('industrial_photography', 'عکاسی صنعتی'),
        ('editor', 'تدوینگر'),
        ('frontend_dev', 'برنامه نویس front'),
    ]

    STAFF_COUNT_CHOICES = [
        ('under_10', 'زیر 10 نفر'),
        ('11_50', '11 تا 50 نفر'),
        ('51_100', '51 تا 100 نفر'),
        ('101_200', '101 تا 200 نفر'),
        ('201_500', '201 تا 500 نفر'),
    ]


    karfarma = models.OneToOneField(Karfarma, on_delete=models.CASCADE)
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
    activity_area = models.CharField(max_length=50, choices=ACTIVITY_CHOICES) # حوزه فعالیت

    # تعداد کارمندان و سال تأسیس
    number_of_employees = models.CharField(max_length=10, choices=STAFF_COUNT_CHOICES)  # تعداد کارمندان
    year_of_establishment = models.IntegerField(blank=True, null=True)  # سال تأسیس

    # تصاویر و ویدیوها
    profile_background_image = models.ImageField(upload_to='backgrounds/', blank=True, null=True)  # تصویر پس‌زمینه پروفایل
    media = models.FileField(upload_to='media/', blank=True, null=True)  # تصاویر یا ویدیوهای سازمان

    created_at = models.DateTimeField(auto_now_add=True) # زمان ثبت‌نام
    
    def __str__(self):
        return self(all)

class JobPosting(models.Model):
    GENDER_CHOICES = [
        ('no_body','مهم نیست'),
        ('male', 'مرد'),
        ('female', 'زن'),
    ]
    EMPLOYMENT_TYPE_CHOICES = [
        ('full_time', 'تمام وقت'),    # تمام وقت
        ('part_time', 'پاره وقت'),    # پاره وقت
        ('remote', 'دورکاری'),          # دورکاری
        ('internship', 'کارآموزی'),  # کارآموزی
        ('project_based', 'پروژه ای'),  # پروژه‌ای
    ]

    MILITARY_STATUS_CHOICES = [
        ('no_matter', 'مهم نیست'),
        ('completed', 'پایان خدمت'),
        ('student_exemption', 'معافیت تحصیلی'),
        ('permanent_exemption', 'معافیت دائم'),
    ]

    SALARY_CHOICES = [
        ('negotiable', 'توافقی'),
        ('minimum_wage', 'حقوق پایه(وزارت کار)'),
        ('9_12_million', 'بین 9 تا 12 میلیون تومان'),
        ('12_20_million', 'بین 12 تا 20 میلیون تومان'),
        ('20_35_million', 'بین 20 تا 35 میلیون تومان'),
        ('35_60_million', 'بین 35 تا 60 میلیون تومان'),
        ('above_60_million', 'بالای 60 میلیون تومان'),
    ]

    EDUCATION_CHOICES = [
        ('no_matter', 'مهم نیست'),
        ('diploma', 'دیپلم'),
        ('associate', 'کاردانی'),
        ('bachelor', 'کارشناسی'),
        ('master', 'کارشناسی ارشد'),
        ('phd', 'دکترا'),
    ]

    organization = models.ForeignKey(Organization,on_delete=models.CASCADE, null=True )

    title = models.CharField(max_length=255)  # عنوان آگهی شغلی
    description = models.TextField()  # توضیحات مربوط به شغل
    location = models.CharField(max_length=255)  # محل کار
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)  # جنسیت
    employment_type= models.CharField(max_length=20 , choices=EMPLOYMENT_TYPE_CHOICES , blank=True)  # نوع استخدام
    military_service_status = models.CharField(max_length=20, choices=MILITARY_STATUS_CHOICES)  # وضعیت خدمت نظام وظیفه
    salary = models.CharField(max_length=20, choices=SALARY_CHOICES)  # حقوق
    state = models.CharField(max_length=100)  # استان
    city = models.CharField(max_length=100)  # شهر
    minimum_educational_qualification = models.CharField(max_length=20, choices=EDUCATION_CHOICES)  # حداقل مدرک تحصیلی
    #address = models.CharField(max_length=255)  # آدرس
    job_skill = models.ManyToManyField('Job_skill', related_name='job_postings')  # مهارت شغلی
    benefits_and_facilities = models.ManyToManyField('Benefits_And_Facilities')  # مزایا و تسهیلات
    posted_date = models.DateField(auto_now_add=True)  # تاریخ انتشار آگهی  

    def __str__(self):
        return self.title
    
class Job_skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency_level = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Benefits_And_Facilities(models.Model):
    name = models.CharField(max_length=100 , null=True , blank= True)

    def __str__(self):
        return self.name

class Product(models.Model):
    # ارتباط با کارفرما (Karfarma)
    karfarma = models.ForeignKey('Karfarma', on_delete=models.CASCADE, related_name='products')

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

class Karjo(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    # ...

class Resume(models.Model):

    karjo = models.OneToOneField('karjo', on_delete=models.CASCADE, related_name='resumes')  # کارجو

    MARITAL_STATUS_CHOICES = [
        ('single', 'مجرد'),  # وضعیت مجرد
        ('married', 'متاهل'),  # وضعیت متاهل
    ]

    GENDER_CHOICES = [
        ('male', 'مرد'),
        ('female', 'زن'),
    ]

    #job_title = models.CharField(max_length=255, verbose_name="عنوان شغلی")  # عنوان شغلی
    about = models.TextField(verbose_name="درباره من")  # توضیح کوتاه درباره خود
    #experience = models.TextField(verbose_name="تجربه کاری")  # تجربه کاری
    #projects = models.TextField(verbose_name="پروژه‌ها")  # پروژه‌ها 
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="تاریخ تولد")  # تاریخ تولد
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES, verbose_name="وضعیت تاهل")  # وضعیت تاهل
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)  # جنسیت
    city = models.CharField(max_length=100, verbose_name="شهر")  # شهر
    state = models.CharField(max_length=100, verbose_name="استان")  # استان
    address = models.TextField(verbose_name="آدرس")  # آدرس
    educational_level = models.ManyToManyField('Educational_Level')# سطح تحصیلات
    organization_name = models.ManyToManyField('Organization_Name') #  سازمان
    skill = models.ManyToManyField('Job_skill_Resume')  # مهارت
    instagram_address = models.URLField(null=True, blank=True, verbose_name="آدرس اینستاگرام")  # آدرس اینستاگرام
    linkedin_address = models.URLField(null=True, blank=True, verbose_name="آدرس لینکدین")  # آدرس لینکدین
    github_address = models.URLField(null=True, blank=True, verbose_name="آدرس گیت‌هاب")  # آدرس گیت‌هاب
    resume_attachment = models.FileField(upload_to='resumes/', null=True, blank=True, verbose_name="بارگذاری رزومه")  # بارگذاری رزومه


    def __str__(self):
        return f"Resume of {self.full_name}"

    class Job_skill_Resume(models.Model):
        name = models.CharField(max_length=100)
        proficiency_level = models.IntegerField(default=0)

        def __str__(self):
            return self.name
    
class Educational_Level(models.Model):
    educational_level = models.CharField(max_length=100, verbose_name="سطح تحصیلات")  # سطح تحصیلات
    field_of_study = models.CharField(max_length=100, verbose_name="رشته تحصیلی")  # رشته تحصیلی
    university_name = models.CharField(max_length=255, verbose_name="نام دانشگاه/مؤسسه")  # نام دانشگاه/مؤسسه
    education_start_date = models.DateField(null=True, blank=True, verbose_name="تاریخ شروع تحصیلات")  # تاریخ شروع تحصیلات
    education_end_date = models.DateField(null=True, blank=True, verbose_name="تاریخ پایان تحصیلات")  # تاریخ پایان تحصیلات

    def __str__(self):
        return self.educational_level
        
class Organization_Name(models.Model):
    organization_name = models.CharField(max_length=255, verbose_name="نام سازمان")  # نام سازمان
    job_start_date = models.DateField(null=True, blank=True, verbose_name="تاریخ شروع کار")  # تاریخ شروع کار
    job_end_date = models.DateField(null=True, blank=True, verbose_name="تاریخ پایان کار")  # تاریخ پایان کار

class blog(models.Model):
    pass