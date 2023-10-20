from django.db import models
from django.urls import reverse

class Chap(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  sum1 = models.IntegerField(default=0) # called
  sum2 = models.IntegerField(default=0) # called fail
  lr = models.CharField(max_length=2, default="L")  # Links or Rechts
  rs = models.CharField(max_length=2, default="r")  # random or serial
  toCallNum0 = models.IntegerField(default=0) # for serial calls

  def get_absolute_url(self):
    return reverse('chapters:chap_detail', kwargs={'pk':self.pk})

  def __str__(self):
    return '(id: ' + str(self.id) + ') ' + self.name + '(' + str(self.pairs.count()) +'/' + str(self.sum1) + '/' + str(self.sum2) + ')'


class Pair(models.Model):
  chap = models.ForeignKey('chapters.Chap', on_delete=models.CASCADE, related_name='pairs')
  textL = models.CharField(max_length=200)
  textR = models.CharField(max_length=200)
  status = models.IntegerField(default=0, blank=True)
  # 1: abgefragt OK, 2: abgefragt falsche Antwort

  # wird ausgegeben, wenn man das object pair anspricht
  def __str__(self):
    return "{0}: TextL = {1}; TextR = {2}; Status = {3}; ID={4},"\
      .format(self.chap.name, self.textL, self.textR, self.status, self.id)


class Call(models.Model):
  textAnswered = models.CharField(max_length=200)
  pairAskedID = models.IntegerField(default=0)
  callType = models.IntegerField(default=0) # All, Rest, Fail comes from button in chap_detail

  def __str__(self):
    return "pairAskedID = {0}: textAnswered = {1}; callType = {2};"\
      .format(self.pairAskedID, self.textAnswered, self.callType)

class IChap(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  name = models.CharField(max_length=200)

  def __str__(self):
    return '(id: ' + str(self.id) + ') ' + self.name + '(' + str(self.Ipairs.count()) + ')'


class IPair(models.Model):
  chap = models.ForeignKey('chapters.IChap', on_delete=models.CASCADE, related_name='Ipairs')
  textL = models.CharField(max_length=200)
  textR = models.CharField(max_length=200)
  status = models.IntegerField(default=0, blank=True)

  def __str__(self):
    return "{0}: TextL = {1}; TextR = {2}; ID={3},"\
      .format(self.chap.name, self.textL, self.textR, self.id)