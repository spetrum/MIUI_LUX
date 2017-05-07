import common
import edify_generator

def RemoveDeviceAssert(info):
  edify = info.script
  for i in xrange(len(edify.script)):
    if "ro.product" in edify.script[i]:
      edify.script[i] = """assert(getprop("ro.product.device") == "lux" || getprop("ro.build.product") == "lux" || getprop("ro.product.device") == "lux_uds" || getprop("ro.build.product") == "lux_uds" || getprop("ro.product.device") == "xt1562" || getprop("ro.build.product") == "xt1562" || getprop("ro.product.device") == "xt1563" || getprop("ro.build.product") == "xt1563" || abort("This package is for device: lux,lux_uds,xt1562,xt1563; this device is " + getprop("ro.product.device") + "."););
unmount("/data");
unmount("/system");"""
      return

def AddAssertions(info):
   edify = info.script
   for i in xrange(len(edify.script)):
    if " ||" in edify.script[i] and ("ro.product.device" in edify.script[i] or "ro.build.product" in edify.script[i]):
      edify.script[i] = edify.script[i].replace(" ||", ' ')
      return

def AddArgsForFormatSystem(info):
  edify = info.script
  for i in xrange(len(edify.script)):
    if "format(" in edify.script[i] and "/dev/block/platform/msm_sdcc.1/by-name/system" in edify.script[i]:
      edify.script[i] = 'format("ext4", "EMMC", "/dev/block/platform/msm_sdcc.1/by-name/system", "0", "/system");'
      return

def WritePolicyConfig(info):
  try:
    file_contexts = info.input_zip.read("META/file_contexts")
    common.ZipWriteStr(info.output_zip, "file_contexts", file_contexts)
  except KeyError:
    print "warning: file_context missing from target;"

def FullOTA_InstallEnd(info):
    WritePolicyConfig(info)
    RemoveDeviceAssert(info)

def IncrementalOTA_InstallEnd(info):
    RemoveDeviceAssert(info)
