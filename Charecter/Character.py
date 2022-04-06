import Level
import Weapons
import ElementalSkill
import ElementalBurst
import NormalAttack
import FirstPassive
import SecondPassive
import ThirdPassive


class Character:

    def __init__(self, baseHealPoints=100, baseAttack=100, baseDefense=100, name="testName"):
        # base stats
        self.level = Level
        self.name = name
        self.baseHealPoints = baseHealPoints
        self.baseAttack = baseAttack
        self.baseDefense = baseDefense

        # real stats
        self.healPoints = baseHealPoints
        self.attack = baseAttack
        self.defense = baseDefense

        # advanced stats
        self.critRate = 0.05
        self.critDMG = 0.5
        self.healBonus = 0
        self.incomeHealBonus = 0
        self.energyRecharge = 1
        self.elementalMastery = 0

        # elemental stats

        # DMG Bonuses
        self.physicalDMGBonus = 0
        self.anemoDMGBonus = 0
        self.cryoDMGBonus = 0
        self.dendroDMGBonus = 0
        self.electroDMGBonus = 0
        self.geoDMGBonus = 0
        self.hydroDMGBonus = 0
        self.pyroDMGBonus = 0

        # damage resist
        self.physicalResistance = 0
        self.anemoResistance = 0
        self.cryoResistance = 0
        self.dendroResistance = 0
        self.electroResistance = 0
        self.geoResistance = 0
        self.hydroResistance = 0
        self.pyroResistance = 0

        # hidden stats
        self.cooldownReduction = 1
        self.shieldStrength = 1
        self.movementSpeed = 1
        self.attackSpeed = 1
        self.staminaConsumption = 1
        self.interruptionResistance = 1
        self.damageReduction = 1

        # logic stats
        # some stuff about weapon
        self.weapon = Weapons

        # skills
        self.elementalSkill = ElementalSkill
        self.elementalBurst = ElementalBurst
        self.normalAttack = NormalAttack
        self.firstPassive = FirstPassive
        self.secondPassive = SecondPassive
        self.thirdPassive = ThirdPassive


    def take_experience(self, amoun):
        self.level = amoun
