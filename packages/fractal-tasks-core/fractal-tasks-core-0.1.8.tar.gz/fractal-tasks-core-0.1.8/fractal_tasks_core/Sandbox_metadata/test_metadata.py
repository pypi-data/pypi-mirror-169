import sys
sys.path.append("../")

from metadata_parsing import parse_yokogawa_metadata  # noqa
from metadata_parsing import read_metadata_files # noqa
from metadata_parsing import read_mrf_file # noqa
import pandas as pd  # noqa


folder = "large/"
folder = "small/"

mlf_path = folder + "MeasurementData.mlf"
mrf_path = folder + "MeasurementDetail.mrf"
# site_metadata, total_files = parse_yokogawa_metadata(mrf_path, mlf_path)
# print(total_files)
# print(site_metadata)
mrf_ref, mlf_ref, error_count_ref = read_metadata_files(mrf_path, mlf_path)

print("*" * 80)


mrf = read_mrf_file(mrf_path)
pd.testing.assert_frame_equal(mrf_ref, mrf)

ns = {"bts": "http://www.yokogawa.co.jp/BTS/BTSSchema/1.0"}
mlf = pd.read_xml(mlf_path, xpath=".//bts:MeasurementRecord", namespaces=ns)

# Remove ERR and non-IMG entries
num_ERR = (mlf.Type == "ERR").sum()
num_non_IMG = (mlf.Type != "IMG").sum()

mlf.drop(mlf[mlf.Type == "ERR"].index, inplace=True)
mlf.drop(mlf[mlf.Type != "IMG"].index, inplace=True)
print(f"Removed {num_ERR} Type=ERR rows")
print(f"Removed {num_non_IMG} Type!=IMG rows")
print()

print(mlf)
