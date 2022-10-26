from django.db import models
from django.contrib.auth.models import AbstractUser

class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default = True, db_index = True, verbose_name = 'Has been activated ?')
    send_messages = models.BooleanField(default = True, verbose_name = 'Send update messages ?')
    paid_account = models.BooleanField(default = False)
    
    class Meta(AbstractUser.Meta):
        pass

class AllBackTests(models.Model	):
    strategy_name = models.CharField(max_length=50, verbose_name='Strategy.')
    owner = models.ForeignKey(AdvUser, verbose_name='Test owner.', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Test data.')
    
    parts = minimal_roi1_time = models.IntegerField(verbose_name="Pairs part")
    minimal_roi1_time = models.IntegerField()
    minimal_roi1_value = models.DecimalField(max_digits=3, decimal_places=1)
    minimal_roi2_time = models.IntegerField()
    minimal_roi2_value = models.DecimalField(max_digits=3, decimal_places=1)
    minimal_roi3_time = models.IntegerField()
    minimal_roi3_value = models.DecimalField(max_digits=3, decimal_places=1)
    minimal_roi4_time = models.IntegerField()
    minimal_roi4_value = models.DecimalField(max_digits=3, decimal_places=1)
    arg_N =  models.IntegerField(verbose_name="Series length (N)")
    arg_R =  models.IntegerField(verbose_name="Persen of same candles (R)")
    arg_P =  models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Price incriase in N candles (P)")
#    arg_P =  models.IntegerField(verbose_name="Price incriase in N candles (P)")
    arg_MR =  models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Movement ROI (MR)")
    stoploss = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Stop-loss (after 0 min)")
    my_stoploss_time = models.IntegerField(verbose_name="My Stop-loss time (after [n] min)")
    my_stoploss_value = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="My Stop-loss value (after [n] min)")
    arg_stoploss =  models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Dsired Stop-loss value (S)")
    max_open_trades = models.IntegerField(verbose_name="Max open trades:")
    text_log = models.TextField(verbose_name="Loggin text")
    hyperopt = models.BooleanField(verbose_name="Hyper opt", default=False)
    
    # for MACD strategy
    buy_cci = models.IntegerField(verbose_name="Buy side: CCI between -700 and 0:")
    sell_cci = models.IntegerField(verbose_name="Sell side: CCI between 0 and 700:")
    
    #for Smooth Scalp strategy
    buy_adx = models.IntegerField(verbose_name="Buy side: ADX between 20 and 50: ")
    buy_adx_enable = models.BooleanField(verbose_name="ADX buy enable: ", default=True)
    sell_adx = models.IntegerField(verbose_name="Sell side: ADX between 50 and 100: ")
    sell_adx_enable = models.BooleanField(verbose_name="ADX sell enable: ", default=False)
    
    buy_fastd = models.IntegerField(verbose_name="Buy side: FastD between 15 and 45: ")
    buy_fastd_enable = models.BooleanField(verbose_name="FastD buy enable: ", default=True)
    sell_fastd = models.IntegerField(verbose_name="Sell side: FastD between 50 and 100: ")
    sell_fastd_enable = models.BooleanField(verbose_name="FastD sell enable: ", default=True)
    
    buy_fastk = models.IntegerField(verbose_name="Buy side: FastK between 15 and 45: ")
    buy_fastk_enable = models.BooleanField(verbose_name="FastK buy enable: ", default=False)
    sell_fastk = models.IntegerField(verbose_name="Sell side: FastK between 50 and 100: ")
    sell_fastk_enable = models.BooleanField(verbose_name="FastK sell enable: ", default=True)
    
    buy_mfi = models.IntegerField(verbose_name="Buy side: MFI between 10 and 25: ")
    buy_mfi_enable = models.BooleanField(verbose_name="MFI buy enable: ", default=True)
    sell_mfi = models.IntegerField(verbose_name="Sell side: MFI between 50 and 100: ")
    sell_mfi_enable = models.BooleanField(verbose_name="MFI sell enable: ", default=False)
    
    sell_cci_scalp = models.IntegerField(verbose_name="Sell side: CCI between 100 and 200: ")
    sell_cci_scalp_enable = models.BooleanField(verbose_name="CCI sell enable: ", default=True)
    
    class Meta():
        verbose_name_plural = "BackTest settings"
        verbose_name = "BackTest settings"
        ordering = ['-created_at']

class DataBufer(models.Model):
    name = models.CharField(max_length=20)
    user_strategy_choise = models.IntegerField()

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return '%s:%d' %(self.name, self.user_strategy_choise)
#        return '%s (%s)' % (self.name, self.user_strategy_choise)

    def delete_everything(self):
        DataBufer.objects.all().delete()
    
#class Person(models.Model):
#    name = models.CharField(max_length=20)
#    age = models.IntegerField()


