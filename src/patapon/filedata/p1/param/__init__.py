from patapon.filedata.patapon_data_class import PataponDataClass

from .damageparam import DamageParam
from .squadactivityparam import SquadActivityParam

# systemdata
from .abnormalstatusparam import AbnormalStatusParam
from .carnivalpowerevalutateparam import CarnivalPowerEvalutateParam
from .carnivalpowerevalutateparambases import CarnivalPowerEvalutateParamBases
from .charabirthparam import CharaBirthParam
from .charagroupparam import CharaGroupParam
from .cookingparam import CookingParam
from .effectparam import EffectParam
from .gameparam import GameParam
from .hiteffecttableparam import HitEffectTableParam
from .instructioncommandparam import InstructionCommandParam
from .laboparam import LaboParam
from .miracleparam import MiracleParam
from .missionparam import SystemDataMissionParam
from .particleparam import ParticleParam
from .soundgameparam import SoundGameParam
from .soundparam import SoundParam
from .squadlineparam import SquadLineParam
from .systemparam import SystemParam

# basesdata
from .charaparam import BasesDataCharaParam
from .facilitypersonparam import FacilityPersonParam
from .nodenameparam import NodeNameParam
from .weaponequipparam import WeaponParam

# gamedata
from .motiontimingparam import MotionTimingParam
from .motiontypeparam import MotionTypeParam
from .squadactivityparam import SquadActivityParam
from .squadctrlfuncparam import SquadCtrlFuncParam
from .unitlayoutparam_e import UnitLayoutParamE

# folder-specific
from .actorparam import ActorParam
from .charaparam import CharaParam
from .weaponequipparam import EquipParam
from .missionparam import MissionParam
from .nodenameparam import NodeName
from .unitparam import UnitParam


def get_dataclass_from_filename(name: str) -> tuple[type[PataponDataClass]|None,int]:
    data_filename_mapping: dict[str,type[PataponDataClass]] = {
        'abnormalstatusparam.dat': AbnormalStatusParam,
        'carnivalpowerevalutateparam.dat': CarnivalPowerEvalutateParam,
        'carnivalpowerevalutateparambases.dat': CarnivalPowerEvalutateParamBases,
        'charabirthparam.dat': CharaBirthParam,
        'charagroupparam.dat': CharaGroupParam,
        'cookingparam.dat': CookingParam,
        'effectparam.dat': EffectParam,
        'gameparam.dat': GameParam,
        'hiteffecttableparam.dat': HitEffectTableParam,
        'instructioncommandparam.dat': InstructionCommandParam,
        'laboparam.dat': LaboParam,
        'miracleparam.dat': MiracleParam,
        'missionparam.dat': SystemDataMissionParam,
        'particleparam.dat': ParticleParam ,
        'soundgameparam.dat': SoundGameParam,
        'soundparam.dat': SoundParam,
        'squadlineparam.dat': SquadLineParam,
        'systemparam.dat': SystemParam,
        'charaparam.dat': BasesDataCharaParam,
        'facilityparam.dat': FacilityPersonParam,
        'nodenameparam.dat': NodeNameParam,
        'personparam.dat': FacilityPersonParam,
        'weaponparam.dat': WeaponParam,
        'motiontimingparam.dat': MotionTimingParam,
        'motiontypeparam.dat': MotionTypeParam,
        'squadactivityparam.dat': SquadActivityParam,
        'squadcrtlfuncparam.dat': SquadCtrlFuncParam,
        'unitparam.dat': UnitParam,
        'unitlayoutparam_e.dat': UnitLayoutParamE,
    }

    specific_folder_filename_mapping: dict[str,type[PataponDataClass]] = {
        'charaparam.dat': CharaParam,
        'equipparam.dat': EquipParam,
        'missionparam.dat': MissionParam,
        'actorparam.dat': ActorParam
    }

    cls = data_filename_mapping.get(name, None)
    if cls is not None:
        return cls, 1
    
    cls = specific_folder_filename_mapping.get(name, None)
    if cls is not None:
        return cls, 2

    return cls, 0