from django.db import models

class Products(models.Model):

    Material_Choice=[('S','Silk'),
    ('C','Cotton')]

    Clothe_Choice=[('SA','Saree'),
    ('KU','Kurta'),
    ('DU','Dupatha'),]
    Category_Choice=[('CKS', 'Chanderi Kataan Silk'),
('CSK','Chanderi Silk Cotton'),
('CSS','Chanderi Soft Silk'),
('KaSC','Kanchipuram Silk Cotton'),
('KuSC','Kuppadam Silk Cotton'),
('LC','Linen Cotton'),
('SL','Silk Linen')]

    Vendor_Choice=[('KS','KS'),
    ('RM','RM'),
    ('AP','AP'),]

    Title       = models.CharField(max_length=200)
    Description = models.TextField()
    Material    = models.CharField(max_length = 100, choices = Material_Choice, default = 'C')
    Clothe_Type = models.CharField(max_length = 100, choices = Clothe_Choice, default = 'SA')
    Category    = models.CharField(max_length = 100, choices = Category_Choice, default = 'CKS')
    Vendor      = models.CharField(max_length = 100, choices = Vendor_Choice, default = 'KS')
    Price       = models.DecimalField(max_digits = 100 ,decimal_places = 2, default=0 )
    Offer       = models.BooleanField(default=False)
    Image       = models.ImageField(upload_to='pics')
    #ks, rm, ap
    

    





