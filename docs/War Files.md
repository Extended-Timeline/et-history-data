# War Files

War data is recorded in yml format as shown below.

```
sample_war:
  1234.5.6:
    #Name "first MOR conquest of TLE"
    name: "NORMAL_WAR_NAME"
	ordinal: 1
	
	#CB
	war_type: take_province
	cb_type: conquer_province
	casus_belli: cb_conquer_province
	target: tlemcen
	
	#Participants
	MOR:
	  side: attacker
	  reason: instigator
	TFL:
	  side: attacker
	  reason: subject
	  caller: MOR
	TLE:
	  side: defender
	  reason: target
	FPW:
	  side: defender
	  reason: alliance
	  caller: TLE
  1234.6.7:
    action: yes
  1238.8.21:
    FPW:
	  side: none
  1240:
    truce_length: 60
    action: no
``` 

Truces can also be created without a preceding war.

```
just_a_truce:
  1321:
	MOR:
	  side: attacker
	TFL:
	  side: attacker
	TLE:
	  side: defender
	FPW:
	  side: defender
    action: no
	truce_length: 60
``` 
---

## All allowed arguments with explanations

| Argument | Value type | Required | Explanation | 
|------|----------|----------|----------|
| name | localization key | yes, unless truce | The base name of the war |
| ordinal | integer | yes, unless truce | Sets the ordinal number in the name of the war |
| war_type | war type | yes, unless truce | Type of the war, take_province or superiority |
| cb_type | cb type | yes, unless truce |  |
| casus_belli | cb ID | yes, unless truce | The casus belli used for the war |
| target | country tag/location ID | no | Sets the target if the CB targets a country or a location |
| [country tag] | see table below | no | Sets the status of a country in the war |
| action | yes/no | yes | yes sets action to have started, no sets the war to have ended |
| truce_length | integer | yes | Sets the length of the truce after the war in months |

---

## Arguments under [country tag] section

| Argument | Value type | Required | Explanation | 
|------|----------|----------|----------|
| side | attacker/defender/none | yes | Sets if the country is attacker or defender. Setting this to none removes the country from the war. |
| reason | reason | yes, unless truce | The reason the country joined the war. instigator/target for main participants, subject/alliance for others. |
| caller | country tag | no | The tag of country that called this participant to the war. Not set for primary participants. |

---
