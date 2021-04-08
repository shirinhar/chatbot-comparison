## story_voip-2d3d74d091-20130328_135311
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - utter_request
* inform{"pricerange": "cheap"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-03c2655d43-20130327_194616
* hello
 - utter_welcomemsg
* inform{"food": "korean"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "area"}
 - action_request
 - utter_offer
* bye

## story_voip-fe4b6ef58f-20130325_220934
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"food": "japanese", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_canthelp
* inform{"food": "spanish"}
 - utter_expl-conf
* negate
 - action_suggest
 - utter_canthelp
* reqalts{"food": "spanish"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "spanish"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "signature"}
 - action_request
 - utter_offer
* request{"slot": "signature"}
 - action_request
 - utter_offer
* bye

## story_voip-d225fad9df-20130328_183352
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-b57f8ee22b-20130327_000138
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "north"}
 - utter_request
* inform{"food": "scottish"}
 - utter_request
* inform{"food": "scottish"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "french"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-59bc8a2167-20130325_143706
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform{"food": "christmas"}
 - action_suggest
 - utter_offer
* hello
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-0fa32b1e78-20130328_151336
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform
 - utter_request
* inform
 - utter_request
* inform{"food": "singaporean"}
 - action_suggest
 - utter_offer
* inform{"food": "north american"}
 - utter_expl-conf
* affirm
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-50af5438f1-20130402_084400
* hello
 - utter_welcomemsg
* inform{"food": "gastropub"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - utter_request
* inform{"food": "gastropub"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-a31ca3e355-20130323_223338
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"food": "mediterranean"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-e8997b10da-20130401_152019
* hello
 - utter_welcomemsg
* affirm{"food": "persian", "task": "find"}
 - utter_request
* inform
 - utter_expl-conf
* affirm{"food": "persian", "task": "find"}
 - utter_request
* inform{"food": "persian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "portuguese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "portuguese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "portuguese"}
 - utter_expl-conf
* affirm
 - utter_expl-conf
* negate{"food": "portuguese"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* affirm{"food": "portuguese"}
 - action_suggest
 - utter_offer
* bye

## story_voip-4f069a4136-20130402_031309
* hello
 - utter_welcomemsg
* reqalts{"food": "corsica"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* reqalts{"area": "west"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-22756d9e8f-20130329_045435
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"type": "restaurant", "pricerange": "moderate", "task": "find"}
 - utter_request
* inform{"food": "chinese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-ab4f1dbb59-20130328_180542
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-4660dd9eab-20130329_080055
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform
 - utter_request
* inform
 - utter_request
* inform{"food": "mexican"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-4a6ecc1f1c-20130328_121528
* hello
 - utter_welcomemsg
* inform{"food": "creative", "area": "south", "task": "find"}
 - utter_expl-conf
* affirm{"area": "south"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese", "area": "south"}
 - action_suggest
 - utter_offer
* inform{"food": "chinese"}
 - action_suggest
 - utter_offer
* confirm{"food": "chinese"}
 - action_suggest
 - utter_offer
* inform{"food": "chinese"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-8d5173f3a6-20130324_184603
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "east"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye
 - action_suggest
 - utter_offer
* bye

## story_voip-597cfafdee-20130328_234346
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "west", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"area": "west"}
 - utter_expl-conf
* affirm
 - utter_request
* inform{"food": "international"}
 - action_suggest
 - utter_canthelp
* reqalts{"area": "centre"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-22756d9e8f-20130329_050114
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "task": "find", "area": "centre"}
 - utter_request
* inform{"food": "romanian"}
 - utter_request
* inform{"food": "romanian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "thai"}
 - action_suggest
 - utter_offer
* confirm{"food": "thai"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-317a1436fe-20130325_172154
* hello
 - utter_welcomemsg
* inform{"food": "turkish"}
 - utter_request
* inform
 - utter_request
* inform{"food": "turkish"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-e9b53d6ace-20130401_205843
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform
 - utter_expl-conf
* inform
 - utter_request
* inform{"pricerange": "moderate", "type": "restaurant", "area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-597cfafdee-20130402_010910
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "north", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "moroccan"}
 - utter_request
* inform{"food": "moroccan"}
 - utter_request
* inform{"food": "moroccan"}
 - utter_request
* inform{"food": "asian oriental"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-b6618de447-20130325_145518
* hello
 - utter_welcomemsg
* inform{"area": "east", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-0f41c16f2f-20130401_235017
* hello
 - utter_welcomemsg
* inform{"food": "thai"}
 - utter_request
* inform{"area": "centre"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-31d9d1a567-20130402_035757
* hello
 - utter_welcomemsg
* inform{"pricerange": "dontcare", "food": "korean", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-e0035cc31b-20130326_210405
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "food": "irish", "type": "restaurant"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* inform{"pricerange": "expensive", "food": "italian", "type": "restaurant"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "area"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-bde2721237-20130326_195337
* hello
 - utter_welcomemsg
* inform{"food": "gastropub", "task": "find"}
 - utter_request
* inform{"area": "dontcare"}
 - utter_request
* inform{"food": "gastropub"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "postcode"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-e0035cc31b-20130323_211354
* hello
 - utter_welcomemsg
* inform{"food": "polynesian", "type": "restaurant", "area": "west"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "portuguese"}
 - action_suggest
 - utter_offer
* reqalts{"food": "portuguese"}
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-f091d0e461-20130327_210252
* hello
 - utter_welcomemsg
* hello{"area": "east", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* inform{"pricerange": "moderate", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-e0035cc31b-20130323_210244
* hello
 - utter_welcomemsg
* inform{"area": "east", "type": "restaurant", "task": "find", "food": "barbeque"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian", "type": "restaurant"}
 - action_suggest
 - utter_offer
* reqalts{"food": "indian", "type": "restaurant"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-78f497f314-20130323_144347
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant"}
 - utter_request
* inform{"type": "restaurant"}
 - utter_expl-conf
* negate
 - utter_expl-conf
* negate{"type": "restaurant", "pricerange": "moderate", "task": "find"}
 - utter_expl-conf
* negate
 - utter_expl-conf
* negate
 - utter_request
* inform{"food": "canapes"}
 - utter_request
* inform{"food": "canapes"}
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-4c25da9a27-20130325_181701
* hello
 - utter_welcomemsg
* inform{"food": "polynesian", "type": "restaurant", "area": "north"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-b6618de447-20130328_152908
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-597cfafdee-20130402_011800
* hello
 - utter_welcomemsg
* inform{"area": "north", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "dontcare"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "food"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-187c1708f2-20130325_135219
* hello
 - utter_welcomemsg
* inform{"food": "portuguese"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-2d3d74d091-20130325_221539
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate"}
 - utter_request
* inform
 - utter_request
* inform{"food": "malaysian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye

## story_voip-e8997b10da-20130327_200112
* hello
 - utter_welcomemsg
* inform{"type": "restaurant"}
 - action_suggest
 - utter_canthelp
* inform{"food": "scottish"}
 - action_suggest
 - utter_canthelp
* inform{"food": "british"}
 - utter_expl-conf
* negate{"food": "british"}
 - utter_request
* reqalts{"pricerange": "expensive"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-c8ec8c76dd-20130328_175715
* hello
 - utter_welcomemsg
* inform{"food": "scottish", "type": "restaurant", "task": "find"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* reqalts{"food": "international"}
 - utter_request
* inform{"area": "dontcare"}
 - utter_request
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-936ec6902a-20130328_133128
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant"}
 - utter_request
* inform{"area": "east"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-e72dba1759-20130325_204601
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "west", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "thai"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye

## story_voip-48c12815b3-20130402_051808
* hello
 - utter_welcomemsg
* inform{"food": "greek", "type": "restaurant", "task": "find", "area": "centre"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "french"}
 - action_suggest
 - utter_offer
* confirm{"food": "french"}
 - action_suggest
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-52d599db9c-20130326_214615
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "north"}
 - utter_request
* inform{"food": "catalan"}
 - action_suggest
 - utter_canthelp
* inform{"food": "indian"}
 - utter_request
* inform{"food": "indian"}
 - utter_request
* affirm
 - utter_request
* inform{"food": "indian"}
 - utter_request
* inform{"type": "restaurant", "area": "north"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-b27a230d2e-20130329_033804
* hello
 - utter_welcomemsg
* inform{"food": "chinese", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-869dd52548-20130401_175624
* hello
 - utter_welcomemsg
* inform{"food": "spanish", "pricerange": "expensive", "task": "find"}
 - action_suggest
 - utter_offer
* reqalts{"food": "modern european"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* inform{"task": "find"}
 - utter_expl-conf
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-22756d9e8f-20130329_043954
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-5a464ca603-20130401_193933
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "food": "brazilian"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - utter_request
* inform{"food": "brazilian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "turkish"}
 - action_suggest
 - utter_canthelp
* inform{"food": "turkish", "type": "restaurant"}
 - utter_expl-conf
* inform{"pricerange": "dontcare"}
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - action_suggest
 - utter_select
* inform
 - action_suggest
 - utter_offer
* affirm
 - action_suggest
 - utter_offer
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-ef9aa63b85-20130329_131544
* hello
 - utter_welcomemsg
* inform{"type": "restaurant"}
 - utter_request
* inform
 - utter_request
* inform{"food": "eritrean"}
 - action_suggest
 - utter_select
* negate
 - action_suggest
 - utter_select
* inform{"food": "eritrean"}
 - action_suggest
 - utter_select
* deny{"food": "vietnamese"}
 - utter_request
* inform{"pricerange": "dontcare"}
 - utter_reqmore
* reqalts{"food": "french"}
 - utter_reqmore
* inform{"type": "restaurant", "food": "french"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* thankyou

## story_voip-e99e4f4538-20130327_140746
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"type": "restaurant"}
 - utter_request
* inform{"food": "mexican"}
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye

## story_voip-10beae627f-20130328_165245
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-fdf8b50918-20130329_013925
* hello
 - utter_welcomemsg
* inform{"food": "spanish", "type": "restaurant"}
 - utter_request
* inform
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* bye

## story_voip-62cc0cc55d-20130323_161217
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "task": "find", "area": "centre"}
 - utter_request
* inform{"food": "creative"}
 - action_suggest
 - utter_canthelp
* inform{"food": "international", "type": "restaurant"}
 - action_suggest
 - utter_canthelp
* reqalts{"type": "restaurant", "area": "centre"}
 - action_suggest
 - utter_canthelp
* inform{"food": "international"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone", "slot":  "name"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-8d5173f3a6-20130324_183442
* hello
 - utter_welcomemsg
* inform{"food": "fusion"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "mediterranean"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* inform{"food": "mediterranean"}
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-2e134ee190-20130401_230615
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-8991b7bff6-20130401_174811
* hello
 - utter_welcomemsg
* inform{"type": "restaurant"}
 - utter_request
* inform
 - utter_request
* inform{"food": "canapes"}
 - utter_request
* inform{"food": "turkish"}
 - utter_request
* inform{"food": "turkish"}
 - utter_request
* inform{"pricerange": "moderate"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-db80a9e6df-20130328_230811
* hello
 - utter_welcomemsg
* hello{"area": "west", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "name"}
 - action_request
 - utter_offer
* bye

## story_voip-8991b7bff6-20130401_174015
* hello
 - utter_welcomemsg
* inform{"food": "french"}
 - utter_expl-conf
* inform
 - utter_expl-conf
* inform
 - utter_expl-conf
* inform
 - utter_request
* inform{"food": "french"}
 - utter_expl-conf
* inform
 - utter_expl-conf
* inform
 - utter_request
* inform
 - action_suggest
 - utter_offer
* inform{"food": "french"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-ef9aa63b85-20130329_125741
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant"}
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-e3b4879e0d-20130326_215705
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform
 - action_suggest
 - utter_select
* inform
 - action_suggest
 - utter_select
* inform{"food": "english"}
 - utter_expl-conf
* negate{"food": "english", "task": "find"}
 - utter_expl-conf
* negate{"food": "english"}
 - utter_expl-conf
* inform{"food": "spanish"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "spanish"}
 - action_suggest
 - utter_canthelp
* inform{"food": "spanish"}
 - utter_expl-conf
* negate
 - action_suggest
 - utter_canthelp
* inform{"area": "dontcare"}
 - utter_expl-conf
* negate{"area": "dontcare"}
 - action_suggest
 - utter_select
* inform
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-a8649977cf-20130323_160311
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "food": "mediterranean"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-d7853a398f-20130401_152711
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "food": "afghan"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "korean"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-78f497f314-20130324_203101
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "dontcare"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-5a464ca603-20130401_192625
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "food": "spanish", "task": "find"}
 - utter_expl-conf
* negate{"food": "spanish"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant", "food": "spanish", "task": "find"}
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - utter_expl-conf
* negate
 - utter_expl-conf
* negate{"area": "dontcare"}
 - utter_expl-conf
* negate
 - action_suggest
 - utter_canthelp
* inform{"area": "dontcare"}
 - action_suggest
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-afd3aa91f0-20130325_225729
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "centre"}
 - utter_expl-conf
* inform{"food": "kosher"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* reqalts{"food": "italian"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant", "task": "find"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "italian"}
 - utter_expl-conf
* affirm
 - utter_expl-conf
* affirm
 - utter_request
* inform{"pricerange": "dontcare"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-561b472540-20130328_123209
* hello
 - utter_welcomemsg
* affirm{"pricerange": "cheap", "type": "restaurant", "area": "north"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-59bc8a2167-20130328_130054
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant"}
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-e2a895cfe5-20130326_233655
* hello
 - utter_welcomemsg
* inform{"area": "dontcare", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"area": "dontcare"}
 - utter_request
* inform{"food": "jamaican"}
 - utter_request
* inform{"food": "jamaican"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "thai"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "thai"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-7e22911804-20130324_193050
* hello
 - utter_welcomemsg
* negate
 - utter_request
* inform{"food": "indonesian", "type": "restaurant", "area": "north", "task": "find"}
 - utter_expl-conf
* negate{"area": "north"}
 - utter_expl-conf
* affirm{"area": "north"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "italian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye

## story_voip-ad40cf5489-20130327_192458
* hello
 - utter_welcomemsg
* inform{"food": "caribbean", "type": "restaurant", "area": "west", "task": "find"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-db80a9e6df-20130328_230211
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "area": "east"}
 - utter_request
* inform{"pricerange": "expensive", "type": "restaurant"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-ef9aa63b85-20130328_211048
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"type": "restaurant", "task": "find"}
 - utter_request
* inform
 - utter_request
* inform{"food": "bistro"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "asian oriental"}
 - utter_expl-conf
* affirm
 - utter_request
* inform{"pricerange": "dontcare"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "postcode"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-21ec2b7850-20130325_162417
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap"}
 - utter_request
* inform
 - utter_request
* inform{"food": "mediterranean"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-36440f7305-20130327_195221
* hello
 - utter_welcomemsg
* inform{"food": "spanish", "area": "west"}
 - utter_request
* inform{"area": "west"}
 - utter_request
* inform{"area": "west"}
 - utter_expl-conf
* affirm
 - utter_request
* inform{"food": "spanish"}
 - utter_request
* inform{"food": "spanish"}
 - action_suggest
 - utter_canthelp
* inform{"area": "dontcare"}
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* ack
 - action_suggest
 - utter_offer
* bye

## story_voip-52d599db9c-20130402_001953
* hello
 - utter_welcomemsg
* inform{"food": "chinese", "area": "south"}
 - utter_request
* inform{"food": "chinese"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-d645d56d23-20130324_000651
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "task": "find"}
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - utter_request
* inform{"food": "bistro"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "asian oriental"}
 - action_suggest
 - utter_canthelp
* inform{"food": "asian oriental"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-b20b6e847a-20130326_222030
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant"}
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-2f209793f4-20130326_005104
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "food": "basque"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant", "food": "international"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant", "food": "international"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-aaa44b4121-20130326_051152
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"pricerange": "moderate", "type": "restaurant"}
 - action_suggest
 - utter_select
* inform{"food": "british"}
 - action_suggest
 - utter_select
* inform{"food": "british"}
 - action_suggest
 - utter_select
* inform{"area": "north"}
 - action_suggest
 - utter_canthelp
* inform{"area": "south"}
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* inform
 - utter_expl-conf
* inform{"food": "british"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-da10d74c3e-20130328_142725
* hello
 - utter_welcomemsg
* inform{"area": "south", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "austrian"}
 - utter_request
* inform{"food": "austrian"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* reqalts{"area": "south", "food": "indian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-318851c80b-20130328_220341
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "food": "hungarian", "type": "restaurant"}
 - action_suggest
 - utter_canthelp
* inform{"food": "modern european"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant"}
 - utter_expl-conf
* negate
 - action_suggest
 - utter_canthelp
* inform{"food": "modern european", "type": "restaurant"}
 - utter_expl-conf
* inform{"food": "modern european"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-aaa44b4121-20130327_171617
* hello
 - utter_welcomemsg
* inform{"food": "international", "task": "find"}
 - utter_request
* inform
 - utter_request
* inform{"pricerange": "dontcare"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-03d6592b76-20130326_012615
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "food": "steakhouse"}
 - utter_request
* inform
 - utter_request
* inform{"food": "steakhouse"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* confirm{"food": "steakhouse"}
 - action_suggest
 - utter_offer
* inform{"food": "steakhouse"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "vietnamese"}
 - action_suggest
 - utter_offer
* inform{"food": "vietnamese"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-b772dbf437-20130402_141548
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "centre"}
 - utter_request
* inform{"food": "spanish"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-b772dbf437-20130402_142550
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform{"pricerange": "expensive"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "food"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-8d5173f3a6-20130324_185406
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-21ec2b7850-20130327_042044
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "south"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"area": "south"}
 - utter_expl-conf
* affirm
 - utter_request
* inform{"food": "creative"}
 - action_suggest
 - utter_canthelp
* inform{"food": "chinese"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-922209b777-20130327_011455
* hello
 - utter_welcomemsg
* inform{"food": "european", "pricerange": "expensive", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-935947e17b-20130328_164611
* hello
 - utter_welcomemsg
* inform{"area": "east", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* inform{"food": "chinese", "area": "east"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-7f9c1c8411-20130328_164730
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant"}
 - utter_request
* inform{"area": "east"}
 - utter_request
* request{"slot": "pricerange", "slot":  "type"}
 - action_request
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "postcode"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-dcaeb62b29-20130326_033832
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "area": "south"}
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - utter_request
* inform
 - utter_request
* inform{"pricerange": "expensive"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-14cb91bc48-20130328_163139
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-e9b53d6ace-20130401_190135
* hello
 - utter_welcomemsg
* inform{"area": "west", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-5cf59cc660-20130327_143308
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "food": "greek", "task": "find"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "turkish"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "turkish"}
 - action_suggest
 - utter_offer
* inform{"pricerange": "expensive"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-b57f8ee22b-20130325_173725
* hello
 - utter_welcomemsg
* inform{"type": "restaurant"}
 - utter_request
* inform{"area": "west"}
 - utter_request
* inform{"food": "corsica"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* inform{"food": "italian"}
 - utter_request
* inform
 - action_suggest
 - utter_select
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-fbd422ad18-20130328_184129
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "task": "find"}
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-2d3d74d091-20130401_234343
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform
 - utter_request
* inform{"food": "korean"}
 - action_suggest
 - utter_offer
* inform{"pricerange": "expensive"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-9735278861-20130401_154740
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-869dd52548-20130401_184008
* hello
 - utter_welcomemsg
* inform{"food": "vietnamese"}
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "area"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-72e50baa85-20130327_061918
* hello
 - utter_welcomemsg
* inform{"food": "gastropub", "task": "find"}
 - utter_request
* inform
 - utter_request
* inform{"type": "restaurant"}
 - utter_request
* inform{"food": "gastropub"}
 - utter_expl-conf
* inform{"food": "gastropub"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye
 - utter_repeat
* bye

## story_voip-155e939ebc-20130327_203006
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform{"food": "european"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-0fa32b1e78-20130402_141117
* hello
 - utter_welcomemsg
* inform{"area": "north", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-f22c2bf9c7-20130326_203410
* hello
 - utter_welcomemsg
* inform{"area": "west"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* inform{"food": "corsica"}
 - action_suggest
 - utter_canthelp
* inform{"food": "british"}
 - utter_request
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-bb1fd497eb-20130326_230444
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "food": "fusion"}
 - action_suggest
 - utter_canthelp
* inform{"food": "turkish"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-31de0daa7b-20130401_205633
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "south", "food": "international"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-43479eb5c2-20130323_180515
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "south"}
 - utter_request
* inform{"food": "venetian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "venetian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "portuguese"}
 - utter_expl-conf
* affirm
 - utter_expl-conf
* inform{"food": "portuguese"}
 - utter_expl-conf
* negate
 - action_suggest
 - utter_canthelp
* inform{"food": "portuguese"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-d7853a398f-20130401_154937
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-da10d74c3e-20130328_141500
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "moderate", "task": "find"}
 - utter_request
* inform{"area": "dontcare"}
 - utter_request
* inform{"food": "bistro"}
 - action_suggest
 - utter_canthelp
* confirm{"pricerange": "moderate", "type": "restaurant", "food": "british"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-187c1708f2-20130327_132654
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "area": "east"}
 - utter_request
* inform{"food": "dontcare"}
 - utter_request
* inform{"pricerange": "expensive"}
 - action_suggest
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* inform{"pricerange": "expensive"}
 - action_suggest
 - utter_offer
* inform{"pricerange": "expensive", "type": "restaurant", "area": "east"}
 - action_suggest
 - utter_select
* inform{"pricerange": "expensive"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-73ce546185-20130324_021914
* hello
 - utter_welcomemsg
* inform{"food": "austrian", "type": "restaurant", "area": "dontcare", "task": "find"}
 - utter_request
* inform{"food": "austrian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "mediterranean"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "mediterranean"}
 - utter_expl-conf
* affirm
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-2f4c700ae3-20130401_190757
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "food": "kosher"}
 - action_suggest
 - utter_canthelp
* inform{"food": "modern european"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-8efef4eae9-20130325_234031
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant"}
 - utter_request
* inform
 - utter_request
* inform{"food": "barbeque"}

## story_voip-15d8a89cec-20130327_014753
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "food": "brazilian", "type": "restaurant"}
 - utter_expl-conf
* affirm
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* confirm
 - action_suggest
 - utter_canthelp
* inform{"food": "asian oriental"}
 - action_suggest
 - utter_select
* bye
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-dcaeb62b29-20130327_082220
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "food": "scandinavian"}
 - action_suggest
 - utter_canthelp
* inform{"pricerange": "cheap", "type": "restaurant", "food": "asian oriental"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-bde2721237-20130325_155143
* hello
 - utter_welcomemsg
* inform{"area": "south"}
 - utter_request
* inform{"pricerange": "cheap", "type": "restaurant"}
 - utter_request
* inform{"food": "mexican"}
 - action_suggest
 - utter_canthelp
* inform{"food": "chinese"}
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-4660dd9eab-20130329_080725
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "north", "food": "kosher"}
 - action_suggest
 - utter_offer
* confirm{"food": "kosher"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-f22c2bf9c7-20130328_113940
* hello
 - utter_welcomemsg
* inform{"area": "south"}
 - utter_request
* inform{"pricerange": "expensive"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-199d62165b-20130402_121601
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "west"}
 - utter_request
* inform{"food": "turkish"}
 - action_suggest
 - utter_canthelp
* reqalts{"area": "centre"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "pricerange"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye
 - action_suggest
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-935947e17b-20130402_194703
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* inform{"pricerange": "moderate", "type": "restaurant", "food": "english"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-b20968d1ea-20130323_110621
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant"}
 - utter_request
* inform{"area": "dontcare"}
 - utter_request
* inform{"food": "english"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "turkish"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "turkish"}
 - action_suggest
 - utter_offer
* confirm{"food": "turkish"}
 - utter_expl-conf
* confirm{"food": "turkish"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-e3b4879e0d-20130327_182147
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "expensive", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-e61fa89add-20130327_071630
* hello
 - utter_welcomemsg
* inform{"food": "danish", "area": "south"}
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-aaa44b4121-20130326_054647
* hello
 - utter_welcomemsg
* inform{"food": "traditional", "area": "south"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "italian"}
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-e3b4879e0d-20130326_024455
* hello
 - utter_welcomemsg
* inform{"food": "corsica", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_canthelp
* inform{"food": "vietnamese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "vietnamese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* hello
 - action_suggest
 - utter_canthelp
* bye

## story_voip-3b81cbb287-20130326_025552
* hello
 - utter_welcomemsg
* inform{"food": "japanese", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "modern european"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "modern european"}
 - action_suggest
 - utter_offer
* inform{"pricerange": "moderate", "food": "european"}
 - action_suggest
 - utter_select
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* inform{"food": "modern european"}
 - utter_request
* inform
 - utter_expl-conf
* request{"slot": "food"}
 - action_request
 - utter_offer
* inform{"task": "find"}
 - utter_expl-conf
* inform{"food": "modern european", "type": "restaurant", "task": "find"}
 - utter_expl-conf
* confirm{"pricerange": "moderate"}
 - action_suggest
 - utter_select
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-e72dba1759-20130326_220053
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "dontcare"}
 - utter_request
* inform{"food": "caribbean"}
 - action_suggest
 - utter_canthelp
* inform{"food": "mediterranean"}
 - action_suggest
 - utter_canthelp
* inform{"food": "mediterranean"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-9735278861-20130401_161036
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant"}
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-597cfafdee-20130402_005342
* hello
 - utter_welcomemsg
* inform{"food": "romanian", "type": "restaurant", "pricerange": "cheap", "task": "find"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "portuguese"}
 - action_suggest
 - utter_canthelp
* negate{"food": "portuguese"}
 - action_suggest
 - utter_select
* inform{"food": "portuguese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-9819537952-20130327_021901
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "west"}
 - utter_request
* inform{"food": "traditional"}
 - action_suggest
 - utter_canthelp
* inform{"food": "british"}
 - utter_expl-conf
* affirm
 - utter_request
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye

## story_voip-da4a08ad84-20130328_154358
* hello
 - utter_welcomemsg
* inform{"area": "west", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-583e7cede5-20130323_052525
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant"}
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform
 - utter_expl-conf
* inform{"pricerange": "moderate", "type": "restaurant"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-9f989824fd-20130325_201440
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "north"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-4a6ecc1f1c-20130329_152505
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "north", "food": "christmas"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-561b472540-20130328_124901
* hello
 - utter_welcomemsg
* affirm{"pricerange": "expensive", "type": "restaurant", "food": "african"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-e0035cc31b-20130326_203939
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "food": "barbeque"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "vietnamese"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "vietnamese"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-96f43326a4-20130324_101258
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "dontcare"}
 - utter_expl-conf
* negate
 - utter_expl-conf
* inform{"area": "dontcare"}
 - utter_request
* inform{"food": "international"}
 - utter_expl-conf
* inform
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-9735278861-20130402_140608
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "cheap", "task": "find"}
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-10beae627f-20130401_163221
* hello
 - utter_welcomemsg
* inform{"area": "north", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "scandinavian"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* deny{"food": "indian", "food": "scandinavian"}
 - action_suggest
 - utter_offer
* inform{"food": "scandinavian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "asian oriental"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-f4026333dc-20130327_180235
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "food": "welsh"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "asian oriental"}
 - utter_expl-conf
* inform{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "area"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-8efef4eae9-20130325_230851
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "food": "halal"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - utter_request
* inform{"food": "halal"}
 - action_suggest
 - utter_offer
* repeat
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "postcode"}
 - action_request
 - utter_offer
* repeat
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* repeat
 - action_suggest
 - utter_offer
* repeat
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* repeat
 - action_suggest
 - utter_canthelp
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye
 - action_suggest
 - utter_offer
* bye

## story_voip-0a45bc863d-20130326_204718
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive"}
 - utter_request
* inform
 - utter_request
* inform{"food": "malaysian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "korean"}
 - action_suggest
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-381a50592b-20130326_043457
* hello
 - utter_welcomemsg
* inform{"area": "south"}
 - utter_request
* inform{"area": "south"}
 - utter_expl-conf
* affirm
 - utter_request
* inform{"food": "traditional"}
 - action_suggest
 - utter_canthelp
* inform{"food": "italian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "italian"}
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-fdf8b50918-20130327_024718
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "east", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-dcaeb62b29-20130327_083948
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "west", "food": "moroccan"}
 - utter_request
* inform{"food": "moroccan"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* reqalts{"food": "moroccan"}
 - action_suggest
 - utter_offer
* reqalts{"food": "moroccan"}
 - action_suggest
 - utter_offer
* reqalts{"food": "moroccan"}
 - action_suggest
 - utter_offer
* inform{"food": "moroccan"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-bb1fd497eb-20130326_231928
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "north"}
 - utter_request
* inform{"food": "british"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - action_suggest
 - utter_select
* inform{"area": "north"}
 - action_suggest
 - utter_select
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-be5b7bf9d9-20130402_203757
* hello
 - utter_welcomemsg
* inform{"area": "east", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "gastropub"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-2d2d103292-20130329_040656
* hello
 - utter_welcomemsg
* inform{"area": "east", "food": "japanese", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant", "food": "indian", "task": "find"}
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-7f9c1c8411-20130401_170332
* hello
 - utter_welcomemsg
* affirm
 - utter_request
* inform{"food": "corsica"}
 - action_suggest
 - utter_canthelp
* inform{"food": "asian oriental"}
 - action_suggest
 - utter_canthelp
* inform{"food": "asian oriental"}
 - action_suggest
 - utter_canthelp
* inform{"food": "asian oriental"}
 - utter_expl-conf
* negate
 - action_suggest
 - utter_canthelp
* inform{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-d7aef99178-20130328_184019
* hello
 - utter_welcomemsg
* inform{"area": "north", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-0241bbae39-20130327_194703
* hello
 - utter_welcomemsg
* inform{"area": "south", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - utter_request
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-48c12815b3-20130402_050043
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-158a881c88-20130328_150912
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "west"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-e2a895cfe5-20130327_021102
* hello
 - utter_welcomemsg
* inform{"area": "north", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-58047f5227-20130327_032739
* hello
 - utter_welcomemsg
* inform{"area": "east", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-5cf59cc660-20130328_145134
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "north"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-d645d56d23-20130402_035204
* hello
 - utter_welcomemsg
* inform{"area": "east", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-48c12815b3-20130326_034916
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "expensive", "task": "find"}
 - action_suggest
 - utter_offer
* confirm{"food": "italian"}
 - action_suggest
 - utter_offer
* inform{"type": "restaurant", "pricerange": "expensive", "task": "find"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform{"food": "catalan", "task": "find"}
 - action_suggest
 - utter_canthelp
* inform{"food": "catalan"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant"}
 - action_suggest
 - utter_canthelp
* inform{"food": "italian", "task": "find"}
 - utter_expl-conf
* negate
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform{"food": "italian", "pricerange": "expensive", "task": "find"}
 - action_suggest
 - utter_offer
* confirm{"food": "italian"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* inform{"type": "restaurant", "task": "find", "food": "catalan"}
 - utter_expl-conf
* negate
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* inform{"food": "italian", "task": "find"}
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "area"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-2d2d103292-20130329_035835
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "area": "west"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-e99e4f4538-20130327_144810
* hello
 - utter_welcomemsg
* inform{"area": "south", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"pricerange": "moderate"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-e54437a6f0-20130325_133942
* hello
 - utter_welcomemsg
* inform{"area": "east", "food": "swedish"}
 - action_suggest
 - utter_canthelp
* inform{"food": "chinese"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-ad40cf5489-20130327_192155
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "expensive", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-ec3c3aaf98-20130323_141803
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "moderate", "task": "find"}
 - utter_request
* inform{"area": "dontcare"}
 - utter_request
* inform{"food": "lebanese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* bye

## story_voip-96f43326a4-20130323_071326
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "expensive", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - utter_request
* inform{"type": "restaurant"}
 - utter_request
* inform
 - utter_expl-conf
* negate{"pricerange": "expensive"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* inform{"pricerange": "expensive"}
 - action_suggest
 - utter_offer
* inform{"pricerange": "expensive"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-f32f2cfdae-20130327_013713
* hello
 - utter_welcomemsg
* inform{"area": "west", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "chinese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "british"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-3cf7bd870d-20130328_211947
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-381a50592b-20130326_044413
* hello
 - utter_welcomemsg
* inform{"area": "west"}
 - utter_request
* inform{"area": "west"}
 - utter_request
* inform{"food": "cuban"}
 - utter_request
* inform{"food": "cuban"}
 - utter_request
* inform{"food": "cuban"}
 - utter_request
* inform{"food": "cuban"}
 - utter_expl-conf
* inform
 - utter_request
* inform
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-0a45bc863d-20130325_201117
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-f22c2bf9c7-20130328_120523
* hello
 - utter_welcomemsg
* inform{"food": "mexican"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-3cf7bd870d-20130327_180852
* hello
 - utter_welcomemsg
* reqalts{"area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* inform{"pricerange": "cheap", "type": "restaurant"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-ccf48b9a6a-20130329_052518
* hello
 - utter_welcomemsg
* inform{"area": "west", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "mediterranean"}
 - action_suggest
 - utter_canthelp
* inform{"food": "north american"}
 - action_suggest
 - utter_canthelp
* inform{"food": "italian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-b08f15a787-20130326_021438
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap"}
 - utter_request
* inform{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-10beae627f-20130329_155112
* hello
 - utter_welcomemsg
* inform{"area": "south", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-e30cb521fb-20130328_144608
* hello
 - utter_welcomemsg
* inform{"food": "cuban", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_canthelp
* inform{"food": "chinese"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - utter_expl-conf
* affirm{"food": "chinese"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-31d9d1a567-20130402_034546
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"food": "dontcare"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-bb1fd497eb-20130325_164823
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant"}
 - utter_request
* inform{"food": "traditional"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "spanish"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "spanish"}
 - action_suggest
 - utter_canthelp
* inform{"food": "spanish"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform{"food": "spanish"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-202b6a3cc4-20130327_185351
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant"}
 - utter_request
* inform{"area": "east"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-fe4b6ef58f-20130325_233447
* hello
 - utter_welcomemsg
* inform{"type": "restaurant"}
 - utter_request
* inform{"area": "north"}
 - action_suggest
 - utter_select
* negate{"area": "north"}
 - utter_request
* inform{"food": "world"}
 - action_suggest
 - utter_canthelp
* inform{"food": "chinese"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-8991b7bff6-20130401_180108
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform
 - utter_request
* inform
 - utter_request
* inform{"food": "spanish"}
 - utter_request
* inform{"food": "spanish"}
 - utter_request
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-318851c80b-20130328_224338
* hello
 - utter_welcomemsg
* inform{"food": "basque", "type": "restaurant"}
 - utter_request
* inform
 - utter_request
* inform{"food": "basque"}
 - action_suggest
 - utter_canthelp
* inform
 - utter_expl-conf
* inform{"food": "spanish"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-d7aef99178-20130328_184824
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "east"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-5cf59cc660-20130328_163609
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-4c0d36762a-20130328_204956
* hello
 - utter_welcomemsg
* inform{"area": "east", "pricerange": "expensive", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "dontcare"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-f32f2cfdae-20130327_015213
* hello
 - utter_welcomemsg
* inform{"task": "find"}
 - utter_request
* inform{"food": "crossover", "area": "north"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-f22c2bf9c7-20130328_120123
* hello
 - utter_welcomemsg
* inform{"food": "international"}
 - utter_request
* inform{"area": "centre"}
 - utter_request
* inform{"pricerange": "expensive"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request

## story_voip-e3b4879e0d-20130327_181715
* hello
 - utter_welcomemsg
* inform{"area": "north", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-e54437a6f0-20130325_140049
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform
 - utter_expl-conf
* inform{"pricerange": "expensive"}
 - utter_expl-conf
* affirm{"food": "danish"}
 - utter_expl-conf
* negate{"food": "danish"}
 - action_suggest
 - utter_canthelp
* inform{"food": "danish"}
 - action_suggest
 - utter_offer
* inform{"food": "danish"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* inform{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-7f9c1c8411-20130328_141000
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive"}
 - utter_request
* inform{"pricerange": "expensive", "type": "restaurant"}
 - utter_request
* inform{"food": "cantonese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "north american"}
 - utter_expl-conf
* negate
 - utter_expl-conf
* negate
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* negate
 - utter_expl-conf
* negate
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_offer
* inform{"food": "cantonese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "north american"}
 - action_suggest
 - utter_canthelp
* inform{"food": "north american"}
 - utter_expl-conf
* inform{"food": "north american"}
 - utter_expl-conf
* inform{"food": "north american"}
 - action_suggest
 - utter_canthelp
* inform{"pricerange": "expensive", "food": "north american"}
 - action_suggest
 - utter_canthelp
* inform{"food": "north american"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform{"food": "north american", "type": "restaurant", "pricerange": "expensive"}
 - action_suggest
 - utter_canthelp
* bye

## story_voip-3b81cbb287-20130324_215534
* hello
 - utter_welcomemsg
* inform{"area": "west", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-88b68a9a41-20130323_114000
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "north"}
 - utter_request
* inform{"food": "turkish"}
 - action_suggest
 - utter_canthelp
* reqalts{"area": "dontcare"}
 - action_suggest
 - utter_canthelp
* reqalts{"area": "dontcare"}
 - action_suggest
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-8d5173f3a6-20130323_011736
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate"}
 - utter_request
* inform{"area": "south"}
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-7e07d8f0f5-20130328_191131
* hello
 - utter_welcomemsg
* request{"slot": "area"}
 - action_request
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - utter_request
* inform{"food": "seafood"}
 - action_suggest
 - utter_canthelp
* inform{"food": "italian"}
 - utter_expl-conf
* negate
 - action_suggest
 - utter_canthelp
* inform{"food": "italian"}
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* inform
 - utter_expl-conf
* inform
 - utter_expl-conf
* inform
 - action_suggest
 - utter_canthelp
* request{"slot": "addr"}
 - action_request
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* thankyou
 - action_suggest
 - utter_canthelp
* inform
 - utter_expl-conf
* inform
 - utter_expl-conf
* negate
 - utter_expl-conf
* inform
 - action_suggest
 - utter_canthelp
* thankyou
 - action_suggest
 - utter_canthelp
* bye

## story_voip-2d3d74d091-20130328_140026
* hello
 - utter_welcomemsg
* inform{"area": "north"}
 - utter_request
* inform{"food": "indian"}
 - utter_request
* inform{"food": "indian"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-31d9d1a567-20130402_040402
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "task": "find"}
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform{"area": "north"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-e61fa89add-20130327_074357
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "area": "north"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-14cb91bc48-20130328_162839
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive"}
 - utter_request
* inform
 - utter_expl-conf
* negate
 - utter_expl-conf
* inform{"food": "portuguese"}
 - utter_request
* inform{"food": "portuguese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "mediterranean"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform{"food": "mediterranean"}
 - action_suggest
 - utter_canthelp
* inform{"pricerange": "expensive"}
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* reqalts{"food": "mediterranean"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-7f9c1c8411-20130401_162408
* hello
 - utter_welcomemsg
* inform{"type": "restaurant"}
 - action_suggest
 - utter_canthelp
* inform{"food": "italian", "area": "south"}
 - action_suggest
 - utter_canthelp
* inform{"food": "italian", "area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* thankyou

## story_voip-e54437a6f0-20130326_210856
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"pricerange": "cheap"}
 - utter_request
* inform{"pricerange": "cheap", "type": "restaurant"}
 - utter_request
* inform
 - utter_request
* inform{"food": "lebanese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-03c59ba692-20130402_054245
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "east"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-202b6a3cc4-20130327_184215
* hello
 - utter_welcomemsg
* inform{"food": "korean"}
 - action_suggest
 - utter_canthelp
* inform{"food": "korean"}
 - action_suggest
 - utter_select
* inform{"food": "korean"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-2b66f60368-20130326_203018
* hello
 - utter_welcomemsg
* request{"slot": "signature", "slot": "restaurant", "food": "christmas"}
 - action_request
 - utter_canthelp
* reqalts{"food": "british"}
 - action_suggest
 - utter_canthelp
* inform{"pricerange": "expensive", "type": "restaurant", "food": "british"}
 - utter_expl-conf
* negate
 - action_suggest
 - utter_canthelp
* inform{"pricerange": "expensive", "type": "restaurant", "food": "british"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-e99e4f4538-20130327_152525
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant"}
 - utter_request
* inform{"area": "east"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-05e7a5440b-20130328_215138
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate"}
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-158a881c88-20130328_153956
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "area": "north"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-dd9f7810fd-20130322_222331
* hello
 - utter_welcomemsg
* inform{"area": "west", "food": "welsh", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-d0341706f2-20130329_052811
* hello
 - utter_welcomemsg
* inform{"food": "singaporean", "type": "restaurant", "area": "centre"}
 - action_suggest
 - utter_offer
* inform{"food": "singaporean", "task": "find"}
 - action_suggest
 - utter_offer
* inform{"food": "singaporean"}
 - action_suggest
 - utter_offer
* bye

## story_voip-2d2d103292-20130326_043352
* hello
 - utter_welcomemsg
* inform{"food": "mediterranean", "task": "find"}
 - utter_request
* inform
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-3cf7bd870d-20130327_184051
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "food": "crossover", "area": "west"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "vietnamese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "vietnamese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "vietnamese"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-e8997b10da-20130329_001948
* hello
 - utter_welcomemsg
* affirm{"pricerange": "expensive", "type": "restaurant", "food": "italian"}
 - utter_request
* inform{"area": "centre"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-340dbb333e-20130327_011703
* hello
 - utter_welcomemsg
* inform{"area": "north", "food": "canapes"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform{"food": "indian"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-8991b7bff6-20130401_160325
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform
 - action_suggest
 - utter_select
* inform
 - action_suggest
 - utter_select
* inform
 - action_suggest
 - utter_select
* inform{"pricerange": "cheap"}
 - utter_request
* inform{"area": "east"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-3b81cbb287-20130324_020944
* hello
 - utter_welcomemsg
* inform{"food": "international", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-583e7cede5-20130324_063315
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "north", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-dda7c88c6e-20130323_052950
* hello
 - utter_welcomemsg
* inform{"food": "mexican"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-e99e4f4538-20130328_201948
* hello
 - utter_welcomemsg
* inform{"area": "west", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "mediterranean"}
 - action_suggest
 - utter_canthelp
* inform{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-10beae627f-20130328_171313
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant"}
 - utter_request
* inform
 - utter_request
* inform{"food": "turkish"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-be5b7bf9d9-20130401_152435
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "north"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-bb1fd497eb-20130325_163635
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"food": "basque", "area": "east"}
 - utter_request
* inform{"food": "basque"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-7e07d8f0f5-20130327_174435
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "north"}
 - utter_expl-conf
* affirm
 - utter_request
* inform{"food": "british"}
 - action_suggest
 - utter_canthelp
* inform{"food": "british"}
 - utter_expl-conf
* negate
 - action_suggest
 - utter_canthelp
* inform{"food": "british", "area": "north"}
 - action_suggest
 - utter_canthelp
* bye

## story_voip-48c12815b3-20130326_011113
* hello
 - utter_welcomemsg
* inform{"food": "turkish", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-597cfafdee-20130328_232032
* hello
 - utter_welcomemsg
* inform{"food": "african", "type": "restaurant", "task": "find", "area": "centre"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-be5b7bf9d9-20130402_202555
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "moderate", "task": "find"}
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-52d599db9c-20130326_010952
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "food": "mexican", "type": "restaurant"}
 - action_suggest
 - utter_canthelp
* reqalts{"pricerange": "cheap", "food": "asian oriental", "type": "restaurant"}
 - action_suggest
 - utter_select
* inform{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-e3b4879e0d-20130326_021022
* hello
 - utter_welcomemsg
* inform{"area": "north", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-869dd52548-20130401_180331
* hello
 - utter_welcomemsg
* inform{"area": "north", "pricerange": "cheap", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-3b3edac94d-20130324_201732
* hello
 - utter_welcomemsg
* inform{"food": "french", "type": "restaurant", "area": "north", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-7f9c1c8411-20130328_200359
* hello
 - utter_welcomemsg
* inform{"food": "turkish"}
 - utter_request
* inform
 - utter_request
* inform
 - action_suggest
 - utter_offer
* bye

## story_voip-7e07d8f0f5-20130328_184956
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "south"}
 - utter_expl-conf
* affirm
 - utter_request
* inform{"pricerange": "expensive"}
 - utter_expl-conf
* affirm{"pricerange": "expensive"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-78f497f314-20130324_140601
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "task": "find"}
 - utter_request
* inform{"area": "dontcare"}
 - utter_request
* inform{"food": "brazilian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "gastropub"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "gastropub"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "area"}
 - action_request
 - utter_offer
* inform{"area": "west"}
 - action_suggest
 - utter_offer
* bye

## story_voip-869dd52548-20130401_184559
* hello
 - utter_welcomemsg
* inform{"food": "japanese", "area": "centre"}
 - utter_request
* inform{"food": "cantonese"}
 - utter_request
* inform{"food": "cantonese"}
 - utter_request
* inform{"food": "cantonese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "international"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-199d62165b-20130402_123401
* hello
 - utter_welcomemsg
* inform{"area": "north", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-4c25da9a27-20130325_183445
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "south", "food": "moroccan"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* reqalts{"food": "modern european"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "modern european"}
 - action_suggest
 - utter_offer
* confirm{"food": "modern european"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* reqalts{"food": "european"}
 - action_suggest
 - utter_canthelp
* inform{"area": "centre"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-59bc8a2167-20130328_130810
* hello
 - utter_welcomemsg
* inform{"food": "thai"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_canthelp
* inform{"food": "british"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-d645d56d23-20130323_222004
* hello
 - utter_welcomemsg
* inform{"food": "european", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "area"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-14f776f781-20130329_033249
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-58047f5227-20130327_034311
* hello
 - utter_welcomemsg
* inform{"food": "seafood", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - utter_request
* inform{"food": "seafood"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-be5694f464-20130328_125916
* hello
 - utter_welcomemsg
* affirm{"area": "north", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "cantonese"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-3b59a0391b-20130401_134901
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform
 - utter_request
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-dd9f7810fd-20130322_225458
* hello
 - utter_welcomemsg
* inform{"food": "canapes", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* confirm{"food": "canapes"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* reqalts{"food": "turkish", "type": "restaurant"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-fce37b0ccb-20130328_145014
* hello
 - utter_welcomemsg
* inform{"food": "basque", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - utter_expl-conf
* affirm
 - utter_request
* inform{"area": "west"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-52eb280e7b-20130325_125522
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform{"pricerange": "cheap"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-87de4f7a80-20130324_154807
* hello
 - utter_welcomemsg
* hello{"area": "east", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-4a6ecc1f1c-20130329_153749
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "area": "north"}
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-0fa32b1e78-20130328_233747
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "food": "portuguese", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_offer
* inform{"food": "chinese"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-7fdb5b39e7-20130328_222225
* hello
 - utter_welcomemsg
* inform{"food": "spanish", "task": "find"}
 - utter_expl-conf
* negate{"food": "spanish"}
 - utter_request
* inform{"food": "spanish"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-db80a9e6df-20130328_234234
* hello
 - utter_welcomemsg
* inform{"area": "north", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-b27a230d2e-20130323_042544
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "expensive", "task": "find"}
 - utter_request
* inform
 - utter_request
* inform{"food": "seafood"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-2c217000af-20130328_224206
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "area": "south"}
 - utter_request
* inform{"food": "dontcare"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-52d599db9c-20130327_175215
* hello
 - utter_welcomemsg
* thankyou
 - utter_request
* inform{"food": "german"}
 - action_suggest
 - utter_canthelp
* inform{"food": "french"}
 - utter_request
* inform
 - action_suggest
 - utter_select
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-ddcaad92a1-20130326_012016
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "expensive", "task": "find"}
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye

## story_voip-e9b53d6ace-20130324_220734
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "food": "turkish", "task": "find"}
 - utter_request
* inform
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-d7853a398f-20130402_153534
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "food": "international"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-3b59a0391b-20130401_133524
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant"}
 - action_suggest
 - utter_offer
* inform{"area": "east"}
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_canthelp
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-7e07d8f0f5-20130327_180412
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "north"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-db80a9e6df-20130328_231545
* hello
 - utter_welcomemsg
* hello{"pricerange": "cheap", "task": "find"}
 - utter_request
* inform{"type": "restaurant"}
 - utter_request
* inform
 - utter_request
* inform
 - action_suggest
 - utter_offer
* confirm{"type": "restaurant"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* confirm{"type": "restaurant"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* inform{"name": "rice house"}
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-560cbd32a5-20130401_143827
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "area": "south"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* inform{"pricerange": "moderate", "type": "restaurant"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* inform

## story_voip-78f497f314-20130324_201211
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "south", "food": "persian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "portuguese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "portuguese"}
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-922209b777-20130327_004226
* hello
 - utter_welcomemsg
* inform{"area": "east", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-7e07d8f0f5-20130327_175512
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant"}
 - utter_request
* inform
 - utter_request
* inform{"type": "restaurant"}
 - action_suggest
 - utter_canthelp
* inform{"food": "gastropub"}
 - action_suggest
 - utter_canthelp
* inform{"food": "gastropub"}
 - action_suggest
 - utter_canthelp
* bye

## story_voip-cfd5fa34d9-20130402_074254
* hello
 - utter_welcomemsg
* inform{"food": "mexican"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-2d2d103292-20130328_195103
* hello
 - utter_welcomemsg
* inform{"area": "east", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-5a464ca603-20130401_130854
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant"}
 - utter_request
* inform{"area": "dontcare"}
 - utter_expl-conf
* repeat
 - utter_request
* inform{"food": "cantonese"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "north american"}
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-876ef67873-20130327_035101
* hello
 - utter_welcomemsg
* hello{"type": "restaurant", "task": "find"}
 - utter_request
* inform{"area": "dontcare"}
 - utter_request
* inform{"food": "singaporean"}
 - action_suggest
 - utter_offer
* inform{"food": "singaporean", "task": "find"}
 - action_suggest
 - utter_offer
* reqalts{"food": "european"}
 - action_suggest
 - utter_offer
* inform{"type": "restaurant"}
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_canthelp
* bye

## story_voip-187c1708f2-20130325_133750
* hello
 - utter_welcomemsg
* inform{"food": "european", "type": "restaurant"}
 - utter_request
* inform{"area": "dontcare"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-4f069a4136-20130402_032750
* hello
 - utter_welcomemsg
* reqalts{"food": "international"}
 - utter_request
* inform{"area": "south"}
 - action_suggest
 - utter_canthelp
* reqalts{"area": "centre"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-d645d56d23-20130401_204424
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform{"food": "world"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "food", "slot": "name"}
 - action_request
 - utter_offer
* inform{"food": "chinese", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-52eb280e7b-20130326_215044
* hello
 - utter_welcomemsg
* inform{"food": "international"}
 - utter_request
* inform{"area": "centre"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-b08f15a787-20130402_074900
* hello
 - utter_welcomemsg
* inform{"area": "east"}
 - utter_request
* inform
 - utter_request
* inform{"pricerange": "expensive"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-be5b7bf9d9-20130402_201144
* hello
 - utter_welcomemsg
* inform{"food": "cuban", "task": "find"}
 - action_suggest
 - utter_canthelp
* inform{"food": "asian oriental", "task": "find"}
 - action_suggest
 - utter_select
* inform{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* confirm{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-3be3bda933-20130327_014120
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform
 - utter_request
* inform{"pricerange": "expensive"}
 - action_suggest
 - utter_offer
* inform{"area": "south"}
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* inform{"area": "south"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* inform{"area": "south"}
 - action_suggest
 - utter_offer
* inform{"area": "west"}
 - action_suggest
 - utter_offer
* inform{"area": "west"}
 - utter_expl-conf
* inform
 - action_suggest
 - utter_offer
* inform{"area": "west"}
 - action_suggest
 - utter_offer
* inform{"area": "south"}
 - action_suggest
 - utter_offer
* inform{"area": "south"}
 - action_suggest
 - utter_offer
* inform{"area": "south"}
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* inform{"area": "west"}
 - action_suggest
 - utter_offer
* inform{"area": "west"}
 - action_suggest
 - utter_offer
* inform{"area": "south"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-199d62165b-20130402_115733
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "moderate", "task": "find"}
 - utter_request
* inform{"food": "moroccan"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "turkish"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-6d6587c57d-20130328_235137
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "task": "find"}
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform{"food": "european"}
 - utter_request
* inform{"food": "european"}
 - action_suggest
 - utter_canthelp
* reqalts{"area": "centre"}
 - utter_expl-conf
* negate
 - utter_expl-conf
* negate
 - action_suggest
 - utter_canthelp
* inform{"area": "centre", "food": "european", "type": "restaurant", "task": "find"}
 - utter_request
* bye

## story_voip-dcaeb62b29-20130327_082120
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "south"}
 - utter_request
* inform{"food": "portuguese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-b6618de447-20130328_155531
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "food": "hungarian"}
 - utter_request
* inform
 - utter_request
* inform{"food": "hungarian"}
 - utter_expl-conf
* negate
 - action_suggest
 - utter_offer
* inform{"task": "find"}
 - action_suggest
 - utter_offer
* inform{"task": "find"}
 - action_suggest
 - utter_offer
* confirm{"food": "hungarian"}
 - action_suggest
 - utter_offer
* inform{"food": "hungarian", "pricerange": "expensive", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* confirm{"food": "hungarian"}
 - action_suggest
 - utter_offer
* reqalts{"food": "british"}
 - action_suggest
 - utter_offer
* inform{"pricerange": "expensive", "type": "restaurant"}
 - action_suggest
 - utter_select
* inform{"food": "british"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-4a6ecc1f1c-20130328_125150
* hello
 - utter_welcomemsg
* inform{"food": "basque", "type": "restaurant"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "spanish"}
 - action_suggest
 - utter_select
* inform{"food": "spanish"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-05e7a5440b-20130328_212037
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-583e7cede5-20130323_055421
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "north"}
 - utter_request
* inform{"food": "barbeque"}
 - action_suggest
 - utter_canthelp
* inform{"food": "french"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-dcaeb62b29-20130326_041709
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform
 - utter_request
* inform{"food": "belgian"}
 - utter_request
* inform{"food": "belgian"}
 - utter_request
* inform{"food": "belgian"}
 - utter_expl-conf
* negate{"food": "belgian"}
 - utter_request
* inform
 - utter_request
* inform
 - utter_reqmore
* inform{"type": "restaurant", "food": "belgian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "korean"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-d76f6e4f82-20130327_201839
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"food": "mexican"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-50af5438f1-20130327_042937
* hello
 - utter_welcomemsg
* inform{"type": "restaurant"}
 - utter_expl-conf
* negate{"pricerange": "cheap", "type": "restaurant"}
 - utter_expl-conf
* negate{"area": "south"}
 - utter_expl-conf
* inform{"area": "south"}
 - utter_request
* inform{"pricerange": "cheap"}
 - utter_request
* inform
 - utter_expl-conf
* negate
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* inform{"area": "south"}
 - action_suggest
 - utter_offer
* inform{"area": "south"}
 - action_suggest
 - utter_canthelp
* inform{"area": "south"}
 - action_suggest
 - utter_offer
* inform{"area": "south"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* inform{"area": "south"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-88f198881b-20130326_032851
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "north"}
 - utter_request
* inform{"food": "chinese"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* inform{"pricerange": "cheap"}
 - action_suggest
 - utter_offer
* inform{"pricerange": "cheap"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "postcode"}
 - action_request
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* bye

## story_voip-affbf578cf-20130401_162946
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-b27a230d2e-20130323_050439
* hello
 - utter_welcomemsg
* inform{"area": "east", "pricerange": "expensive", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-90732b027d-20130401_215925
* hello
 - utter_welcomemsg
* inform{"food": "traditional"}
 - action_suggest
 - utter_canthelp
* inform{"food": "modern european"}
 - utter_request
* inform{"area": "dontcare"}
 - utter_request
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-f17e3b578c-20130328_174548
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive"}
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* inform{"type": "restaurant"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye

## story_voip-0fa32b1e78-20130328_151950
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform
 - utter_request
* inform{"area": "south"}
 - utter_expl-conf
* negate
 - utter_expl-conf
* negate
 - utter_expl-conf
* inform{"area": "south"}
 - utter_request
* inform
 - utter_request
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-0fa32b1e78-20130402_142022
* hello
 - utter_welcomemsg
* inform{"food": "austrian", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "portuguese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "portuguese"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-6dbc3573bc-20130328_193508
* hello
 - utter_welcomemsg
* inform{"area": "dontcare", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "gastropub"}
 - utter_request
* inform
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-96f43326a4-20130323_073316
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "moderate", "task": "find"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-9f989824fd-20130325_201956
* hello
 - utter_welcomemsg
* inform{"area": "east"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - utter_request
* inform{"pricerange": "cheap"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye
 - utter_repeat
* bye

## story_voip-7e22911804-20130328_164203
* hello
 - utter_welcomemsg
* inform{"food": "swedish", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* confirm{"food": "swedish"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "asian oriental"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* confirm{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* inform{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye
 - utter_repeat
* bye

## story_voip-03d6592b76-20130326_014855
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "food": "halal"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "gastropub"}
 - action_suggest
 - utter_offer
* confirm{"food": "gastropub"}
 - action_suggest
 - utter_offer
* inform{"type": "restaurant", "food": "gastropub"}
 - action_suggest
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-4c25da9a27-20130327_140126
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "east"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-0f41c16f2f-20130402_005804
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant"}
 - action_suggest
 - utter_offer
* inform{"food": "korean"}
 - action_suggest
 - utter_canthelp
* bye

## story_voip-d0341706f2-20130329_022056
* hello
 - utter_welcomemsg
* inform{"food": "italian", "type": "restaurant", "area": "west", "task": "find"}
 - utter_request
* inform{"area": "west"}
 - utter_request
* negate
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-d76f6e4f82-20130327_184807
* hello
 - utter_welcomemsg
* inform{"type": "restaurant"}
 - utter_request
* inform{"food": "greek"}
 - action_suggest
 - utter_canthelp
* inform{"food": "indian"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-9819537952-20130328_235404
* hello
 - utter_welcomemsg
* request{"slot": "pricerange"}
 - action_request
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform{"food": "dontcare"}
 - utter_request
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-a617b6827c-20130323_165831
* hello
 - utter_welcomemsg
* inform{"food": "british", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"area": "south"}
 - action_suggest
 - utter_canthelp
* reqalts{"area": "centre"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-a7ddefaeb3-20130328_172838
* hello
 - utter_welcomemsg
* inform{"type": "restaurant"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"area": "south"}
 - action_suggest
 - utter_select
* inform{"area": "south"}
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - utter_request
* inform
 - utter_request
* inform
 - utter_request
* inform{"pricerange": "expensive"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-fe2783c40a-20130401_145146
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"pricerange": "cheap", "type": "restaurant"}
 - utter_request
* inform{"pricerange": "cheap", "type": "restaurant"}
 - action_suggest
 - utter_offer
* inform{"food": "seafood"}
 - action_suggest
 - utter_offer
* inform{"food": "seafood"}
 - action_suggest
 - utter_canthelp
* inform{"food": "portuguese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-58047f5227-20130326_030552
* hello
 - utter_welcomemsg
* inform{"food": "danish", "type": "restaurant", "area": "west", "task": "find"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-4a6ecc1f1c-20130328_124608
* hello
 - utter_welcomemsg
* inform{"food": "spanish", "task": "find"}
 - utter_request
* inform
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* reqalts{"food": "spanish"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_canthelp
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-d66e12b45c-20130327_173320
* hello
 - utter_welcomemsg
* inform{"area": "north"}
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform{"area": "north"}
 - utter_request
* bye

## story_voip-e2a895cfe5-20130325_232606
* hello
 - utter_welcomemsg
* inform{"food": "kosher", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-90732b027d-20130327_173620
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant"}
 - utter_request
* inform{"area": "dontcare"}
 - utter_expl-conf
* affirm
 - utter_request
* inform{"food": "corsica"}
 - action_suggest
 - utter_canthelp
* inform{"food": "asian oriental"}
 - action_suggest
 - utter_select
* inform{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-583e7cede5-20130324_062107
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "food": "european"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-d645d56d23-20130324_000123
* hello
 - utter_welcomemsg
* inform{"area": "dontcare", "type": "restaurant", "task": "find"}
 - utter_expl-conf
* inform
 - utter_request
* inform{"food": "unusual"}
 - action_suggest
 - utter_canthelp
* inform{"food": "spanish"}
 - utter_expl-conf
* repeat
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-0f41c16f2f-20130325_204340
* hello
 - utter_welcomemsg
* inform{"food": "persian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "indian"}
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform{"pricerange": "cheap"}
 - action_suggest
 - utter_canthelp
* bye

## story_voip-aaa44b4121-20130327_170849
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"pricerange": "cheap"}
 - utter_request
* inform{"pricerange": "cheap"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* inform{"pricerange": "cheap", "type": "restaurant"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-340dbb333e-20130325_231614
* hello
 - utter_welcomemsg
* inform{"food": "african"}
 - utter_request
* inform{"area": "dontcare"}
 - utter_request
* inform{"food": "african"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-7e4cdce06a-20130323_130824
* hello
 - utter_welcomemsg
* inform{"area": "west", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "international"}
 - action_suggest
 - utter_canthelp
* reqalts{"area": "centre"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-249d0f617b-20130326_005503
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_select
* affirm
 - action_suggest
 - utter_select
* inform{"pricerange": "moderate"}
 - utter_expl-conf
* affirm
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* bye

## story_voip-90732b027d-20130401_195651
* hello
 - utter_welcomemsg
* inform{"area": "east"}
 - utter_request
* inform
 - utter_request
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-14cb91bc48-20130327_190136
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform
 - utter_request
* inform
 - utter_request
* inform
 - utter_request
* inform
 - utter_expl-conf
* inform
 - utter_expl-conf
* inform
 - utter_request
* inform
 - utter_request
* inform
 - utter_request
* inform{"food": "brazilian"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant"}
 - action_suggest
 - utter_canthelp
* reqalts{"pricerange": "moderate"}
 - action_suggest
 - utter_offer
* bye

## story_voip-e9b53d6ace-20130401_202659
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "north"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "food"}
 - action_request
 - utter_offer
* request{"slot": "addr", "slot":  "food"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-7e22911804-20130324_190421
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-0f41c16f2f-20130325_213951
* hello
 - utter_welcomemsg
* inform{"food": "fusion"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform{"food": "vietnamese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-597cfafdee-20130328_231005
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "task": "find"}
 - utter_request
* negate
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* inform{"area": "north", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-05e7a5440b-20130328_220724
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform
 - utter_request
* inform{"food": "vegetarian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "european"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-03c2655d43-20130327_192312
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "west"}
 - utter_request
* inform{"food": "swiss"}
 - action_suggest
 - utter_canthelp
* inform{"food": "vietnamese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "vietnamese"}
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-31de0daa7b-20130402_132633
* hello
 - utter_welcomemsg
* inform{"food": "corsica"}
 - utter_request
* inform
 - utter_request
* inform{"food": "corsica"}
 - action_suggest
 - utter_canthelp
* inform{"food": "gastropub"}
 - action_suggest
 - utter_canthelp
* inform{"food": "gastropub", "type": "restaurant"}
 - action_suggest
 - utter_canthelp
* inform{"food": "gastropub"}
 - utter_expl-conf
* affirm
 - utter_expl-conf
* negate
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* inform{"food": "gastropub"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "gastropub"}
 - utter_expl-conf
* affirm
 - utter_expl-conf
* inform{"food": "gastropub"}
 - action_suggest
 - utter_canthelp
* bye

## story_voip-72e50baa85-20130326_052642
* hello
 - utter_welcomemsg
* inform{"food": "chinese"}
 - utter_expl-conf
* affirm{"area": "south"}
 - utter_request
* inform{"pricerange": "cheap"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* inform
 - action_suggest
 - utter_canthelp
* bye

## story_voip-317a1436fe-20130325_171321
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive"}
 - utter_request
* inform
 - utter_request
* inform{"food": "basque"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* inform{"food": "basque"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* inform{"food": "basque"}
 - action_suggest
 - utter_offer
* inform{"food": "korean"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-935947e17b-20130328_165646
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant"}
 - action_suggest
 - utter_offer
* inform{"pricerange": "cheap", "type": "restaurant"}
 - utter_request
* inform{"food": "german"}
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* reqalts{"food": "european"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* reqalts{"food": "european"}
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* inform
 - utter_expl-conf
* affirm
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* reqalts{"food": "portuguese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* affirm
 - action_suggest
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye

## story_voip-935947e17b-20130402_202004
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "moderate", "task": "find"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* request{"slot": "food", "slot":  "area"}
 - action_request
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_canthelp
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-90732b027d-20130327_181557
* hello
 - utter_welcomemsg
* inform{"food": "greek"}
 - action_suggest
 - utter_canthelp
* inform{"food": "turkish"}
 - action_suggest
 - utter_offer
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-d0341706f2-20130329_012808
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "expensive", "task": "find"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-922209b777-20130325_160141
* hello
 - utter_welcomemsg
* inform{"area": "east", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-869dd52548-20130326_000655
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-8991b7bff6-20130326_231508
* hello
 - utter_welcomemsg
* inform{"area": "east"}
 - utter_request
* inform
 - utter_request
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye

## story_voip-b08f15a787-20130402_074726
* hello
 - utter_welcomemsg
* inform{"food": "european"}
 - utter_request
* inform{"area": "west"}
 - action_suggest
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-21ec2b7850-20130326_114409
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive"}
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform
 - utter_expl-conf
* inform{"pricerange": "expensive"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-72e50baa85-20130327_062822
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "cheap", "task": "find"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_canthelp
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-50af5438f1-20130327_031854
* hello
 - utter_welcomemsg
* inform{"type": "restaurant"}
 - utter_request
* inform{"area": "centre"}
 - utter_request
* inform{"food": "spanish"}
 - utter_request
* inform{"pricerange": "cheap"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-597cfafdee-20130328_234727
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "task": "find", "area": "centre"}
 - utter_request
* inform{"food": "eritrean"}
 - utter_request
* inform{"pricerange": "cheap"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-e61fa89add-20130326_013931
* hello
 - utter_welcomemsg
* inform{"food": "venetian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "asian oriental"}
 - action_suggest
 - utter_select
* inform{"food": "asian oriental"}
 - utter_request
* inform{"area": "dontcare"}
 - utter_request
* inform{"type": "restaurant"}
 - action_suggest
 - utter_offer
* inform
 - utter_repeat
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-249d0f617b-20130328_161219
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform
 - utter_expl-conf
* affirm{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-05e7a5440b-20130328_214746
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "east", "food": "italian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-2f4c700ae3-20130401_193033
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-e72dba1759-20130325_215313
* hello
 - utter_welcomemsg
* affirm
 - utter_request
* inform{"type": "restaurant", "area": "west", "food": "crossover"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "italian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "italian"}
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - action_suggest
 - utter_select
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-340dbb333e-20130325_233348
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "food": "japanese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "chinese"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-72e50baa85-20130327_060348
* hello
 - utter_welcomemsg
* inform{"area": "west", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-318851c80b-20130328_214609
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-50af5438f1-20130402_081345
* hello
 - utter_welcomemsg
* inform{"area": "south"}
 - utter_request
* inform{"area": "south"}
 - action_suggest
 - utter_select
* inform{"area": "south"}
 - utter_expl-conf
* affirm
 - utter_request
* inform{"food": "basque"}
 - action_suggest
 - utter_canthelp
* inform{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-3cf7bd870d-20130327_181243
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-be5b7bf9d9-20130401_155148
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-9735278861-20130401_160600
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"type": "restaurant", "food": "english"}
 - action_suggest
 - utter_canthelp
* inform{"food": "modern european"}
 - action_suggest
 - utter_canthelp
* inform{"food": "modern european"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "modern european"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-2f4c700ae3-20130401_191755
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "food": "mexican"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-afd3aa91f0-20130325_231946
* hello
 - utter_welcomemsg
* inform{"area": "west", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "thai"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-5a464ca603-20130401_165953
* hello
 - utter_welcomemsg
* inform{"area": "east", "pricerange": "expensive", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-21ec2b7850-20130327_043931
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant"}
 - utter_request
* inform
 - utter_request
* inform{"food": "european"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-b27a230d2e-20130329_040014
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "moderate", "task": "find"}
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye

## story_voip-d7853a398f-20130402_154628
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-bde2721237-20130325_164032
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-b20968d1ea-20130323_111539
* hello
 - utter_welcomemsg
* inform{"type": "restaurant"}
 - utter_request
* inform
 - utter_request
* inform{"area": "dontcare"}
 - utter_expl-conf
* affirm
 - utter_request
* inform{"food": "french"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-b08f15a787-20130402_072532
* hello
 - utter_welcomemsg
* inform{"area": "south"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"pricerange": "moderate"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-52d599db9c-20130402_000814
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant"}
 - utter_request
* inform
 - utter_request
* inform{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* inform{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-50af5438f1-20130402_081208
* hello
 - utter_welcomemsg
* inform{"food": "thai"}
 - utter_request
* inform
 - utter_request
* inform{"food": "thai"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-39a25ab2f8-20130326_131509
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "area": "west"}
 - utter_expl-conf
* affirm
 - utter_expl-conf
* affirm
 - utter_request
* inform{"pricerange": "cheap", "type": "restaurant"}
 - utter_request
* bye

## story_voip-7e07d8f0f5-20130327_181435
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "west"}
 - utter_request
* inform{"food": "international"}
 - utter_request
* inform{"food": "international"}
 - action_suggest
 - utter_canthelp
* inform{"area": "centre"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-4c25da9a27-20130327_140438
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-b27a230d2e-20130329_031422
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "task": "find", "area": "centre"}
 - utter_request
* inform{"food": "european"}
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-d7853a398f-20130401_160153
* hello
 - utter_welcomemsg
* inform{"area": "east"}
 - utter_request
* inform{"food": "indonesian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-f1e8236264-20130323_004330
* hello
 - utter_welcomemsg
* inform{"area": "east", "pricerange": "expensive", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-187c1708f2-20130327_132257
* hello
 - utter_welcomemsg
* inform{"food": "barbeque", "area": "west"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform{"food": "vietnamese"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-0abf414c0c-20130326_235444
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate"}
 - utter_request
* inform{"area": "west"}
 - utter_request
* inform{"area": "west"}
 - utter_request
* inform{"area": "west"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-88b68a9a41-20130324_004031
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "south", "food": "cuban"}
 - utter_request
* inform{"food": "cuban"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "portuguese"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-31de0daa7b-20130401_203534
* hello
 - utter_welcomemsg
* affirm{"pricerange": "cheap"}
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* inform{"pricerange": "cheap", "type": "restaurant", "area": "north"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-9819537952-20130328_232353
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "west"}
 - utter_request
* inform{"food": "singaporean"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-0241bbae39-20130327_204651
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"area": "south"}
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-fe2783c40a-20130401_150540
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"area": "south"}
 - action_suggest
 - utter_select
* inform{"area": "south"}
 - utter_request
* inform
 - utter_request
* inform{"pricerange": "expensive"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-10beae627f-20130401_163410
* hello
 - utter_welcomemsg
* inform{"area": "north", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "catalan"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian", "type": "restaurant"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-fd0c0fb514-20130328_114152
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "area": "east"}
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-ad40cf5489-20130325_180305
* hello
 - utter_welcomemsg
* inform{"food": "corsica", "type": "restaurant", "task": "find", "area": "centre"}
 - action_suggest
 - utter_canthelp
* inform{"food": "international", "type": "restaurant", "task": "find", "area": "centre"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-2c217000af-20130328_223711
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "south"}
 - utter_request
* inform{"food": "dontcare"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-ef9aa63b85-20130328_190444
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "moderate", "task": "find"}
 - utter_request
* inform{"area": "west"}
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "type"}
 - action_request
 - utter_canthelp
* inform
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-e99e4f4538-20130328_201531
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-263ab0e49f-20130326_104818
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "area": "east"}
 - utter_request
* inform{"food": "dontcare"}
 - action_suggest
 - utter_canthelp
* negate{"pricerange": "moderate"}
 - action_suggest
 - utter_canthelp
* inform{"area": "east"}
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-13ff413553-20130328_174952
* hello
 - utter_welcomemsg
* inform{"area": "west"}
 - utter_request
* inform
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-ec3c3aaf98-20130323_141647
* hello
 - utter_welcomemsg
* inform{"food": "english", "pricerange": "expensive", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_canthelp
* inform{"food": "mediterranean"}
 - action_suggest
 - utter_canthelp
* inform{"food": "mediterranean"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-7f9c1c8411-20130401_161233
* hello
 - utter_welcomemsg
* affirm{"pricerange": "expensive", "type": "restaurant"}
 - utter_request
* inform
 - utter_request
* inform{"food": "catalan"}
 - action_suggest
 - utter_canthelp
* inform{"food": "italian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-f1e8236264-20130323_003719
* hello
 - utter_welcomemsg
* inform{"food": "venetian", "pricerange": "expensive", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_canthelp
* inform{"food": "thai"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "thai"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "thai"}
 - utter_expl-conf
* negate
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform{"food": "thai", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-bb1fd497eb-20130325_163241
* hello
 - utter_welcomemsg
* inform{"food": "malaysian", "area": "south"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-a8649977cf-20130323_160436
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "west"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* bye

## story_voip-9819537952-20130327_023856
* hello
 - utter_welcomemsg
* inform{"area": "west"}
 - utter_request
* inform{"food": "hungarian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "vietnamese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "vietnamese"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye

## story_voip-cfd5fa34d9-20130402_072808
* hello
 - utter_welcomemsg
* inform{"type": "restaurant"}
 - utter_request
* inform{"area": "dontcare"}
 - utter_request
* inform{"food": "seafood"}
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-da10d74c3e-20130326_001047
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "west", "pricerange": "cheap", "type": "restaurant"}
 - utter_request
* inform{"food": "dontcare"}
 - action_suggest
 - utter_offer
* reqalts{"pricerange": "cheap", "type": "restaurant", "area": "west"}
 - action_suggest
 - utter_offer
* reqalts{"type": "restaurant", "area": "west"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-5cf59cc660-20130328_172556
* hello
 - utter_welcomemsg
* inform{"food": "persian", "type": "restaurant", "area": "south"}
 - utter_request
* inform{"food": "persian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "portuguese"}
 - action_suggest
 - utter_offer
* confirm{"food": "portuguese"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-e99e4f4538-20130327_150005
* hello
 - utter_welcomemsg
* inform{"area": "east", "pricerange": "expensive", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-9735278861-20130401_152826
* hello
 - utter_welcomemsg
* inform{"area": "south", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"food": "greek"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - utter_expl-conf
* affirm
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-ccc459b689-20130327_004458
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "cheap", "task": "find"}
 - utter_request
* inform
 - utter_request
* inform{"food": "australian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "european"}
 - action_suggest
 - utter_canthelp
* inform{"food": "european"}
 - action_suggest
 - utter_offer
* confirm{"food": "european"}
 - action_suggest
 - utter_offer
* confirm{"food": "european", "type": "restaurant"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-22756d9e8f-20130329_044234
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "south"}
 - utter_request
* inform{"food": "polynesian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "portuguese"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "portuguese"}
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-aaa44b4121-20130327_002455
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "west"}
 - utter_request
* inform{"food": "british"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-ddcaad92a1-20130325_222532
* hello
 - utter_welcomemsg
* hello{"type": "restaurant", "task": "find"}
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform{"food": "christmas"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* inform{"type": "restaurant", "task": "find"}
 - action_suggest
 - utter_select
* inform{"area": "north"}
 - action_suggest
 - utter_select
* inform{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-d7853a398f-20130402_161739
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "east", "food": "creative"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-58047f5227-20130326_032713
* hello
 - utter_welcomemsg
* inform{"food": "swedish", "type": "restaurant", "area": "dontcare", "task": "find"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* reqalts{"food": "north american"}
 - action_suggest
 - utter_canthelp
* inform{"food": "north american"}
 - utter_expl-conf
* affirm
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-7c3a08072d-20130326_005842
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "food": "english"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant", "food": "british"}
 - action_suggest
 - utter_canthelp
* inform{"food": "british"}
 - action_suggest
 - utter_offer
* confirm{"area": "centre"}
 - action_suggest
 - utter_offer
* confirm{"area": "centre"}
 - action_suggest
 - utter_offer
* inform{"type": "restaurant", "food": "british", "area": "centre"}
 - utter_expl-conf
* affirm
 - utter_request
* inform{"food": "british"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-52eb280e7b-20130326_211923
* hello
 - utter_welcomemsg
* inform{"food": "international"}
 - utter_request
* inform
 - utter_request
* inform{"pricerange": "dontcare"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-fe4b6ef58f-20130325_223854
* hello
 - utter_welcomemsg
* inform{"area": "west", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-b6618de447-20130328_160315
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-560cbd32a5-20130401_144308
* hello
 - utter_welcomemsg
* inform{"food": "afghan"}
 - utter_request
* inform{"food": "afghan"}
 - utter_request
* inform{"food": "afghan"}
 - action_suggest
 - utter_canthelp
* inform{"food": "vietnamese"}
 - action_suggest
 - utter_canthelp
* inform
 - utter_expl-conf
* negate
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform{"food": "vietnamese", "area": "dontcare"}
 - action_suggest
 - utter_offer
* confirm{"pricerange": "cheap"}
 - action_suggest
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye

## story_voip-0fa32b1e78-20130328_153725
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "dontcare"}
 - utter_request
* inform{"food": "corsica"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "vietnamese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "vietnamese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-9f447ce48e-20130328_115123
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "task": "find"}
 - utter_request
* inform
 - utter_expl-conf
* inform
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform{"food": "turkish"}
 - action_suggest
 - utter_canthelp
* inform{"food": "turkish"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-9f989824fd-20130325_203925
* hello
 - utter_welcomemsg
* inform{"area": "south"}
 - utter_request
* inform
 - utter_request
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-90732b027d-20130327_180737
* hello
 - utter_welcomemsg
* inform{"food": "romanian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "portuguese"}
 - utter_request
* inform{"area": "dontcare"}
 - action_suggest
 - utter_offer
* inform{"pricerange": "cheap"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-6dbc3573bc-20130328_192107
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant"}
 - utter_request
* inform
 - utter_request
* inform{"food": "kosher"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "modern european"}
 - action_suggest
 - utter_offer
* bye

## story_voip-2f4c700ae3-20130401_185424
* hello
 - utter_welcomemsg
* inform{"food": "asian oriental", "area": "centre"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "european"}
 - action_suggest
 - utter_canthelp
* inform{"food": "european"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-7e22911804-20130326_142538
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "food": "fusion"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_offer
* confirm{"food": "chinese"}
 - action_suggest
 - utter_offer
* inform{"food": "chinese"}
 - action_suggest
 - utter_offer
* bye

## story_voip-1b51204ef5-20130401_145742
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "dontcare"}
 - utter_request
* inform{"food": "international"}
 - utter_request
* inform{"pricerange": "cheap"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-c8ec8c76dd-20130328_205558
* hello
 - utter_welcomemsg
* inform{"area": "west", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-2c217000af-20130325_222430
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "south", "pricerange": "moderate"}
 - utter_request
* inform{"food": "dontcare"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-e72dba1759-20130326_222550
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-5cf59cc660-20130328_160837
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "food": "corsica"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "vietnamese"}
 - utter_expl-conf
* negate{"food": "vietnamese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-0a45bc863d-20130325_202120
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "food": "belgian"}
 - utter_expl-conf
* negate{"food": "belgian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "british"}
 - utter_request
* inform{"area": "centre"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-03c59ba692-20130324_180022
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* thankyou

## story_voip-e3b4879e0d-20130326_024044
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "moderate", "task": "find"}
 - utter_request
* inform
 - utter_request
* inform{"food": "persian"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* reqalts{"food": "persian"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-583e7cede5-20130324_060901
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "moderate", "task": "find"}
 - utter_request
* inform
 - utter_request
* inform
 - action_suggest
 - utter_select
* inform
 - utter_request
* inform{"food": "turkish"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-22c938c8ba-20130325_124542
* hello
 - utter_welcomemsg
* inform{"food": "indonesian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "italian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "italian"}
 - action_suggest
 - utter_canthelp
* inform{"area": "north"}
 - utter_expl-conf
* negate
 - action_suggest
 - utter_canthelp
* thankyou
 - action_suggest
 - utter_canthelp
* thankyou
 - action_suggest
 - utter_canthelp
* inform
 - utter_expl-conf
* affirm
 - utter_expl-conf
* negate
 - action_suggest
 - utter_canthelp
* inform
 - utter_repeat
* inform{"food": "italian"}
 - utter_expl-conf
* inform
 - action_suggest
 - utter_canthelp
* thankyou
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* inform
 - utter_expl-conf
* affirm
 - utter_expl-conf
* negate
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* bye

## story_voip-3b59a0391b-20130401_133038
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"area": "south"}
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-88b68a9a41-20130322_222725
* hello
 - utter_welcomemsg
* inform{"area": "north", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "greek"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-ccf48b9a6a-20130329_053050
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "west", "food": "cantonese"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform{"food": "italian"}
 - utter_request
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-c8821c664b-20130322_222908
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform
 - utter_request
* inform{"food": "french"}
 - action_suggest
 - utter_canthelp
* inform{"food": "italian"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_canthelp
* request{"slot": "addr"}
 - action_request
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* thankyou

## story_voip-fbd422ad18-20130328_182406
* hello
 - utter_welcomemsg
* inform{"area": "east", "pricerange": "expensive", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "dontcare"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-e0035cc31b-20130326_205626
* hello
 - utter_welcomemsg
* inform{"food": "russian", "type": "restaurant"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "korean", "type": "restaurant"}
 - action_suggest
 - utter_select
* inform{"food": "korean"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-935947e17b-20130402_201340
* hello
 - utter_welcomemsg
* inform{"food": "persian", "task": "find"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform{"pricerange": "dontcare"}
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* inform{"food": "asian oriental"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "addr", "slot":  "postcode"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye

## story_voip-ad40cf5489-20130325_181004
* hello
 - utter_welcomemsg
* inform{"food": "welsh", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_expl-conf
* affirm{"pricerange": "cheap"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform{"food": "mediterranean", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-48c12815b3-20130402_045503
* hello
 - utter_welcomemsg
* inform{"food": "corsica", "task": "find"}
 - action_suggest
 - utter_canthelp
* inform{"food": "gastropub", "task": "find"}
 - action_suggest
 - utter_canthelp
* inform{"food": "gastropub", "task": "find"}
 - utter_expl-conf
* negate{"food": "gastropub", "task": "find"}
 - action_suggest
 - utter_canthelp
* inform{"food": "gastropub", "task": "find"}
 - action_suggest
 - utter_canthelp
* inform{"food": "gastropub"}
 - utter_request
* inform
 - action_suggest
 - utter_select
* inform
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-da10d74c3e-20130328_152552
* hello
 - utter_welcomemsg
* inform{"food": "african", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-8f9fb7a86b-20130328_181534
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "west"}
 - utter_request
* inform{"food": "creative"}
 - action_suggest
 - utter_canthelp
* inform{"food": "thai"}
 - action_suggest
 - utter_select
* inform{"food": "thai"}
 - action_suggest
 - utter_select
* inform{"food": "thai"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* repeat
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* inform{"name": "prezzo"}
 - action_suggest
 - utter_select
* inform{"food": "creative"}
 - action_suggest
 - utter_canthelp
* inform{"food": "thai"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* inform{"name": "prezzo"}
 - action_suggest
 - utter_canthelp
* request{"slot": "name"}
 - action_request
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* ack
 - action_suggest
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye

## story_voip-d7853a398f-20130401_152229
* hello
 - utter_welcomemsg
* inform{"area": "east", "food": "spanish"}
 - action_suggest
 - utter_offer
* confirm{"food": "spanish"}
 - action_suggest
 - utter_offer
* inform{"type": "restaurant"}
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* inform{"food": "spanish"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese", "type": "restaurant"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-5749b16764-20130328_150400
* hello
 - utter_welcomemsg
* inform{"food": "german", "pricerange": "cheap", "task": "find"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "european"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "european"}
 - action_suggest
 - utter_canthelp
* inform{"food": "european", "type": "restaurant", "task": "find"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* bye

## story_voip-e8997b10da-20130327_194306
* hello
 - utter_welcomemsg
* affirm{"type": "restaurant", "area": "north"}
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform{"food": "mediterranean"}
 - action_suggest
 - utter_canthelp
* reqalts{"area": "dontcare"}
 - action_suggest
 - utter_canthelp
* reqalts{"area": "dontcare"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-381a50592b-20130323_233439
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant"}
 - utter_request
* inform
 - utter_request
* inform{"food": "vegetarian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "turkish"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-dd9f7810fd-20130322_232152
* hello
 - utter_welcomemsg
* inform{"area": "west", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-fe2783c40a-20130401_143116
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant"}
 - utter_request
* inform{"area": "north"}
 - utter_request
* negate
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye

## story_voip-3b81cbb287-20130324_015234
* hello
 - utter_welcomemsg
* inform{"food": "scottish", "type": "restaurant", "area": "west", "task": "find"}
 - action_suggest
 - utter_canthelp
* inform{"area": "west", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_canthelp
* inform{"food": "scottish"}
 - action_suggest
 - utter_offer
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* confirm{"food": "indian"}
 - action_suggest
 - utter_offer
* inform{"food": "indian", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-50af5438f1-20130402_085647
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive"}
 - utter_request
* inform
 - utter_request
* inform{"food": "italian"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* inform{"food": "italian"}
 - action_suggest
 - utter_offer
* inform{"food": "italian"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* inform{"food": "italian"}
 - action_suggest
 - utter_offer
* inform{"food": "italian"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-0f41c16f2f-20130401_235748
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant"}
 - utter_request
* inform{"area": "north"}
 - utter_expl-conf
* affirm
 - utter_request
* inform{"food": "fusion"}
 - action_suggest
 - utter_canthelp
* inform{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-2d2d103292-20130326_041008
* hello
 - utter_welcomemsg
* inform{"food": "indonesian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "thai", "task": "find"}
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-d76851034e-20130326_221320
* hello
 - utter_welcomemsg
* repeat
 - utter_request
* inform{"food": "romanian", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* inform{"food": "portuguese"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "portuguese"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-e0035cc31b-20130323_212626
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "east"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-4660dd9eab-20130329_085648
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "west"}
 - utter_request
* inform{"food": "bistro"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "italian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "italian"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-381a50592b-20130326_041932
* hello
 - utter_welcomemsg
* inform{"food": "portuguese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "portuguese"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_canthelp
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-3b81cbb287-20130326_031714
* hello
 - utter_welcomemsg
* inform{"food": "world", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "thai"}
 - action_suggest
 - utter_canthelp
* inform{"pricerange": "dontcare", "food": "thai"}
 - utter_expl-conf
* inform{"food": "thai"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-e9b53d6ace-20130324_222525
* hello
 - utter_welcomemsg
* inform{"area": "north", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-d645d56d23-20130401_203325
* hello
 - utter_welcomemsg
* inform{"food": "russian", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_offer
* confirm{"food": "chinese"}
 - action_suggest
 - utter_offer
* inform{"type": "restaurant", "pricerange": "cheap", "task": "find"}
 - action_suggest
 - utter_select
* inform{"food": "russian"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* inform{"type": "restaurant", "pricerange": "cheap", "task": "find"}
 - action_suggest
 - utter_select
* inform{"food": "chinese"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-90732b027d-20130401_222034
* hello
 - utter_welcomemsg
* inform{"food": "mexican"}
 - action_suggest
 - utter_offer
* inform{"pricerange": "cheap"}
 - action_suggest
 - utter_canthelp
* inform{"food": "vietnamese"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-7e07d8f0f5-20130328_185739
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform
 - utter_request
* inform
 - action_suggest
 - utter_select
* inform
 - utter_request
* affirm
 - action_suggest
 - utter_select
* inform{"area": "north"}
 - action_suggest
 - utter_offer
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_offer
* bye

## story_voip-5cf59cc660-20130327_144338
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "west"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-7f9c1c8411-20130328_210227
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "food": "indian"}
 - utter_expl-conf
* inform
 - utter_request
* inform{"food": "polynesian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "mediterranean"}
 - utter_expl-conf
* negate{"area": "dontcare"}
 - action_suggest
 - utter_canthelp
* inform{"food": "mediterranean", "type": "restaurant"}
 - utter_expl-conf
* negate
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant"}
 - utter_expl-conf
* inform{"area": "dontcare"}
 - action_suggest
 - utter_select
* inform
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-908884f5fd-20130327_000655
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "west", "food": "german"}
 - utter_request
* inform{"food": "german"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "british"}
 - action_suggest
 - utter_canthelp
* bye

## story_voip-a352cb5ca5-20130401_231236
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "west"}
 - utter_request
* inform{"food": "australian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-da10d74c3e-20130326_001657
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "west"}
 - utter_request
* inform{"food": "dontcare"}
 - action_suggest
 - utter_offer
* reqalts{"pricerange": "cheap", "type": "restaurant", "area": "west"}
 - action_suggest
 - utter_offer
* reqalts{"pricerange": "cheap", "type": "restaurant", "area": "west"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-4c0d36762a-20130328_204534
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-aaa44b4121-20130327_170541
* hello
 - utter_welcomemsg
* inform{"food": "malaysian", "area": "centre"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "korean"}
 - action_suggest
 - utter_canthelp
* inform{"food": "korean"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-935947e17b-20130402_202130
* hello
 - utter_welcomemsg
* inform{"area": "north", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-39a25ab2f8-20130329_010257
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform
 - utter_request
* inform
 - utter_expl-conf
* inform{"pricerange": "cheap", "type": "restaurant", "area": "north"}
 - utter_expl-conf
* inform{"pricerange": "cheap"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye
 - action_suggest
 - utter_canthelp
* bye

## story_voip-e99e4f4538-20130327_153656
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "catalan"}
 - utter_request
* inform
 - utter_request
* inform{"food": "catalan"}
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* inform{"food": "gastropub"}
 - action_suggest
 - utter_canthelp
* reqalts
 - utter_expl-conf
* affirm
 - utter_expl-conf
* negate
 - action_suggest
 - utter_canthelp
* reqalts{"food": "gastropub"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant", "food": "gastropub"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-10beae627f-20130328_132217
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform
 - utter_request
* inform{"food": "tuscan", "pricerange": "expensive", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - utter_request
* inform
 - utter_request
* inform
 - action_suggest
 - utter_offer
* inform{"food": "tuscan"}
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* inform{"food": "tuscan", "task": "find"}
 - utter_expl-conf
* inform{"food": "tuscan"}
 - action_suggest
 - utter_offer
* negate
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* negate
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* inform{"food": "tuscan"}
 - action_suggest
 - utter_offer
* inform{"food": "thai"}
 - utter_expl-conf
* inform
 - utter_expl-conf
* inform{"type": "restaurant"}
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* bye

## story_voip-00d76b791d-20130327_005023
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "food": "canapes"}
 - action_suggest
 - utter_canthelp
* inform{"food": "modern european"}
 - utter_request
* inform
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-bde2721237-20130325_162740
* hello
 - utter_welcomemsg
* inform{"food": "belgian", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "chinese"}
 - utter_request
* inform{"area": "north"}
 - action_suggest
 - utter_canthelp
* inform{"area": "south"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-4f069a4136-20130402_033307
* hello
 - utter_welcomemsg
* inform{"food": "vegetarian", "task": "find"}
 - action_suggest
 - utter_canthelp
* inform{"food": "turkish", "type": "restaurant"}
 - action_suggest
 - utter_select
* inform{"food": "turkish"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - utter_request
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-52eb280e7b-20130325_132224
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "east"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-0a45bc863d-20130325_200034
* hello
 - utter_welcomemsg
* inform{"food": "english", "area": "centre"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform{"food": "british"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-f32f2cfdae-20130328_192703
* hello
 - utter_welcomemsg
* inform{"food": "chinese"}
 - utter_request
* inform{"task": "find", "food": "seafood"}
 - utter_request
* inform
 - utter_request
* inform{"food": "seafood"}
 - utter_request
* inform{"food": "seafood"}
 - action_suggest
 - utter_offer
* inform{"food": "seafood"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-187c1708f2-20130327_130329
* hello
 - utter_welcomemsg
* inform{"food": "korean", "pricerange": "moderate"}
 - action_suggest
 - utter_canthelp
* inform{"pricerange": "dontcare"}
 - action_suggest
 - utter_canthelp
* inform{"food": "korean"}
 - action_suggest
 - utter_canthelp
* inform{"food": "korean", "pricerange": "expensive"}
 - action_suggest
 - utter_select
* inform{"pricerange": "expensive"}
 - utter_expl-conf
* inform
 - action_suggest
 - utter_select
* inform{"pricerange": "expensive"}
 - action_suggest
 - utter_select
* inform{"food": "korean", "pricerange": "expensive"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-0fa32b1e78-20130402_132031
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-e9b53d6ace-20130401_200405
* hello
 - utter_welcomemsg
* inform{"area": "south", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "chinese"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-3be3bda933-20130326_131833
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"area": "south"}
 - utter_expl-conf
* inform{"area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* inform{"area": "south"}
 - action_suggest
 - utter_offer
* inform{"area": "west"}
 - action_suggest
 - utter_offer
* inform{"area": "west"}
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* inform{"area": "east"}
 - action_suggest
 - utter_select
* inform{"area": "south"}
 - action_suggest
 - utter_select
* inform{"area": "south"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-3b3edac94d-20130323_202936
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-00d76b791d-20130327_012807
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "food": "venetian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "gastropub"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-00d76b791d-20130327_010906
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "food": "spanish", "type": "restaurant"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-d7aef99178-20130328_184628
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "food": "portuguese"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-3cf7bd870d-20130328_212502
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "centre"}
 - utter_expl-conf
* affirm
 - utter_request
* inform{"food": "kosher"}
 - utter_request
* inform{"food": "kosher"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "italian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "italian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "italian"}
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-5cf59cc660-20130327_144955
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-b27a230d2e-20130329_030324
* hello
 - utter_welcomemsg
* inform{"food": "christmas", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* inform{"food": "christmas"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* inform{"food": "christmas"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* reqalts{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* inform{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-90732b027d-20130327_190315
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"food": "christmas"}
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* inform{"food": "indian"}
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* inform{"pricerange": "cheap"}
 - action_suggest
 - utter_offer
* inform{"pricerange": "cheap"}
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* inform{"pricerange": "cheap"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-fdf8b50918-20130329_035324
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* inform
 - action_suggest
 - utter_canthelp
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-03d6592b76-20130327_025219
* hello
 - utter_welcomemsg
* inform{"food": "austrian", "type": "restaurant", "area": "south"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-fe2783c40a-20130401_145010
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-155e939ebc-20130327_211511
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"pricerange": "cheap", "type": "restaurant", "area": "west"}
 - utter_request
* inform{"food": "dontcare"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-52d599db9c-20130326_212814
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "east", "food": "japanese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "chinese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-935947e17b-20130328_152337
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_canthelp
* thankyou

## story_voip-da4a08ad84-20130328_155250
* hello
 - utter_welcomemsg
* inform{"food": "traditional", "type": "restaurant", "area": "east", "task": "find"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-fdf8b50918-20130326_051921
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-a31ca3e355-20130324_190654
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"pricerange": "moderate"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* inform{"food": "swiss"}
 - action_suggest
 - utter_offer
* inform{"food": "swiss"}
 - action_suggest
 - utter_offer
* inform{"food": "british"}
 - action_suggest
 - utter_offer
* inform{"food": "british"}
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-03c59ba692-20130324_034058
* hello
 - utter_welcomemsg
* inform{"area": "east", "food": "vegetarian", "task": "find"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* inform{"food": "indian", "task": "find"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-ad40cf5489-20130327_191318
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "west", "food": "jamaican"}
 - utter_request
* inform{"food": "jamaican"}
 - action_suggest
 - utter_canthelp
* reqalts{"type": "restaurant", "area": "west", "food": "vietnamese"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant", "food": "vietnamese"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant"}
 - utter_expl-conf
* negate
 - action_suggest
 - utter_offer
* inform{"food": "vietnamese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "vietnamese", "type": "restaurant"}
 - utter_expl-conf
* affirm
 - utter_expl-conf
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-be5b7bf9d9-20130401_151225
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant"}
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-a352cb5ca5-20130401_232817
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate"}
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform
 - utter_request
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-afd3aa91f0-20130325_224706
* hello
 - utter_welcomemsg
* inform{"food": "european", "pricerange": "expensive", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"area": "dontcare"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-48c12815b3-20130326_023109
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"type": "restaurant"}
 - utter_request
* inform{"food": "asian oriental"}
 - utter_expl-conf
* inform{"area": "east", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "asian oriental"}
 - utter_expl-conf
* negate{"food": "asian oriental", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* inform{"food": "asian oriental", "type": "restaurant", "area": "east", "task": "find"}
 - action_suggest
 - utter_offer
* inform{"food": "chinese", "type": "restaurant", "task": "find"}
 - utter_expl-conf
* inform{"food": "chinese", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-3b59a0391b-20130401_135704
* hello
 - utter_welcomemsg
* inform{"area": "west"}
 - utter_request
* inform{"food": "cuban"}
 - action_suggest
 - utter_canthelp
* inform{"food": "indian"}
 - action_suggest
 - utter_offer
* inform{"area": "west"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-e30cb521fb-20130328_135454
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "south"}
 - utter_request
* inform{"area": "south"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* ack{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-31de0daa7b-20130402_133047
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "food": "seafood"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* inform{"food": "chinese"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-876ef67873-20130402_030744
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "food": "world"}
 - action_suggest
 - utter_canthelp
* inform{"food": "british"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-88b68a9a41-20130324_002917
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "west"}
 - utter_request
* inform{"food": "european"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-199d62165b-20130402_122711
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "task": "find", "area": "centre"}
 - utter_request
* inform{"food": "mediterranean"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-62cc0cc55d-20130323_160541
* hello
 - utter_welcomemsg
* inform{"type": "restaurant"}
 - utter_request
* inform{"area": "centre"}
 - utter_request
* inform{"type": "restaurant"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "portuguese"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-f32f2cfdae-20130328_200054
* hello
 - utter_welcomemsg
* inform{"food": "european", "task": "find"}
 - utter_request
* inform
 - utter_request
* inform{"pricerange": "cheap"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "portuguese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "portuguese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-8991b7bff6-20130326_230200
* hello
 - utter_welcomemsg
* inform{"food": "european"}
 - utter_expl-conf
* inform{"food": "european"}
 - utter_request
* inform
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-edb8609855-20130327_182512
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant"}
 - utter_request
* inform
 - utter_request
* inform{"food": "mexican"}
 - action_suggest
 - utter_canthelp
* inform{"food": "international", "type": "restaurant"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-ccf48b9a6a-20130329_042239
* hello
 - utter_welcomemsg
* inform
 - action_suggest
 - utter_select
* inform{"area": "east"}
 - action_suggest
 - utter_select
* inform{"area": "east"}
 - utter_request
* inform{"pricerange": "moderate"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-3b3edac94d-20130324_203209
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone", "slot":  "food"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-7e4cdce06a-20130323_130200
* hello
 - utter_welcomemsg
* inform{"area": "south", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "mexican"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-03d6592b76-20130326_012940
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "food": "turkish"}
 - utter_request
* inform
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - utter_request
* inform{"pricerange": "dontcare"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "postcode"}
 - action_request
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* hello
 - action_suggest
 - utter_canthelp
* bye

## story_voip-30772678da-20130328_193916
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "moderate", "task": "find"}
 - utter_request
* inform
 - utter_request
* inform{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-9f989824fd-20130324_075152
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-f32f2cfdae-20130328_194348
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "cheap", "food": "spanish", "task": "find"}
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-b6618de447-20130328_151535
* hello
 - utter_welcomemsg
* affirm{"type": "restaurant", "pricerange": "expensive", "task": "find"}
 - utter_request
* inform
 - utter_request
* inform{"food": "australian"}
 - action_suggest
 - utter_canthelp
* inform{"pricerange": "expensive", "type": "restaurant", "food": "french"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "french"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-8d5173f3a6-20130323_015026
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "area": "west"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-4660dd9eab-20130329_085958
* hello
 - utter_welcomemsg
* inform{"type": "restaurant"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "korean"}
 - action_suggest
 - utter_select
* inform{"food": "korean"}
 - action_suggest
 - utter_offer
* confirm{"area": "centre"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* bye

## story_voip-fdf8b50918-20130326_050512
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-2d2d103292-20130329_041255
* hello
 - utter_welcomemsg
* inform{"food": "bistro", "task": "find", "area": "centre"}
 - action_suggest
 - utter_canthelp
* inform{"food": "north american", "task": "find"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-14cb91bc48-20130327_204058
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "cheap", "task": "find"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-0f41c16f2f-20130402_005015
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant"}
 - utter_request
* inform{"area": "south"}
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-0fa32b1e78-20130328_233916
* hello
 - utter_welcomemsg
* inform{"area": "east", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "turkish"}
 - action_suggest
 - utter_canthelp
* inform{"area": "dontcare"}
 - action_suggest
 - utter_canthelp
* reqalts{"area": "dontcare"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-2d2d103292-20130329_041636
* hello
 - utter_welcomemsg
* inform{"area": "north", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-edb8609855-20130327_183456
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant"}
 - action_suggest
 - utter_offer
* inform{"area": "west"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-2d3d74d091-20130328_153522
* hello
 - utter_welcomemsg
* inform{"area": "west"}
 - action_suggest
 - utter_select
* inform{"area": "west"}
 - utter_expl-conf
* affirm
 - utter_request
* inform
 - utter_request
* inform{"pricerange": "cheap"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-fce37b0ccb-20130328_143529
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform{"pricerange": "cheap"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-05e7a5440b-20130328_211413
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "east"}
 - utter_request
* inform{"food": "traditional"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-fbd422ad18-20130328_181932
* hello
 - utter_welcomemsg
* inform{"area": "north", "food": "vietnamese", "task": "find"}
 - action_suggest
 - utter_canthelp
* reqalts{"area": "west"}
 - utter_expl-conf
* affirm
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-e72dba1759-20130326_220956
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "moderate", "task": "find"}
 - utter_request
* inform
 - utter_expl-conf
* affirm{"food": "corsica"}
 - action_suggest
 - utter_canthelp
* reqalts{"pricerange": "moderate", "type": "restaurant"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* inform{"food": "indian", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-eaef6f434c-20130323_025908
* hello
 - utter_welcomemsg
* affirm{"area": "north", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform{"food": "belgian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "asian oriental", "type": "restaurant", "area": "north"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-ad40cf5489-20130327_194114
* hello
 - utter_welcomemsg
* inform{"area": "north", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-78f497f314-20130323_142856
* hello
 - utter_welcomemsg
* inform{"area": "west", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye

## story_voip-4f069a4136-20130327_205654
* hello
 - utter_welcomemsg
* inform{"area": "north"}
 - utter_request
* inform
 - utter_expl-conf
* inform{"pricerange": "cheap"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-9f989824fd-20130324_074224
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "area": "north"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-b57f8ee22b-20130325_184849
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "south"}
 - utter_request
* inform{"food": "creative"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* bye

## story_voip-48c12815b3-20130402_052405
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"pricerange": "moderate", "type": "restaurant", "area": "west"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-bde2721237-20130326_193025
* hello
 - utter_welcomemsg
* inform{"food": "world", "task": "find"}
 - action_suggest
 - utter_canthelp
* inform{"food": "vietnamese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-ab4f1dbb59-20130325_214245
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "west", "food": "cuban"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-e3b4879e0d-20130327_030955
* hello
 - utter_welcomemsg
* inform{"food": "polynesian", "task": "find"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "vietnamese"}
 - action_suggest
 - utter_select
* inform{"food": "vietnamese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye

## story_voip-72e50baa85-20130326_045411
* hello
 - utter_welcomemsg
* inform{"food": "cuban"}
 - utter_request
* inform
 - utter_request
* inform{"food": "cuban", "pricerange": "cheap", "type": "restaurant"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* inform{"food": "cuban"}
 - action_suggest
 - utter_offer
* inform{"food": "cuban"}
 - action_suggest
 - utter_offer
* inform{"food": "cuban"}
 - action_suggest
 - utter_offer
* confirm{"food": "cuban"}
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* inform{"food": "cuban"}
 - action_suggest
 - utter_canthelp
* inform{"food": "modern european"}
 - action_suggest
 - utter_select
* inform{"food": "modern european"}
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_canthelp
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye
 - utter_repeat
* bye
 - utter_expl-conf
* bye

## story_voip-59bc8a2167-20130328_132714
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-e8997b10da-20130329_011058
* hello
 - utter_welcomemsg
* affirm{"type": "restaurant", "food": "french"}
 - utter_request
* inform{"area": "centre"}
 - utter_expl-conf
* affirm{"food": "french"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* ack
 - action_suggest
 - utter_canthelp
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* request{"slot": "pricerange"}
 - action_request
 - utter_offer
* ack
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* ack
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_offer
* ack
 - utter_expl-conf
* request{"slot": "addr"}
 - action_request
 - utter_offer
* ack
 - action_suggest
 - utter_offer
* thankyou

## story_voip-31d9d1a567-20130402_042614
* hello
 - utter_welcomemsg
* inform{"area": "north", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"food": "dontcare"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-cfd5fa34d9-20130402_073021
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "pricerange": "cheap", "task": "find"}
 - action_suggest
 - utter_offer
* inform{"area": "east"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-d76f6e4f82-20130327_193430
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "centre"}
 - utter_request
* inform{"food": "spanish"}
 - action_suggest
 - utter_offer
* request{"slot": "phone", "slot":  "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-f1e8236264-20130323_002501
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-6d6587c57d-20130328_140525
* hello
 - utter_welcomemsg
* inform{"food": "scandinavian", "task": "find"}
 - utter_request
* inform{"area": "dontcare"}
 - utter_expl-conf
* affirm
 - utter_request
* inform{"pricerange": "cheap"}
 - action_suggest
 - utter_offer
* inform{"food": "scandinavian"}
 - action_suggest
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* bye

## story_voip-f113dbb0e1-20130322_233310
* hello
 - utter_welcomemsg
* inform{"area": "east", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_select
* inform{"area": "east"}
 - utter_request
* inform{"area": "west"}
 - utter_expl-conf
* inform
 - action_suggest
 - utter_canthelp
* reqalts{"food": "chinese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "chinese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-876ef67873-20130402_031718
* hello
 - utter_welcomemsg
* affirm
 - utter_request
* inform{"area": "dontcare"}
 - utter_request
* inform{"food": "danish"}
 - action_suggest
 - utter_canthelp
* inform{"food": "mediterranean"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-3b3edac94d-20130324_211737
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap", "type": "restaurant", "food": "caribbean"}
 - action_suggest
 - utter_offer
* confirm{"food": "caribbean"}
 - action_suggest
 - utter_offer
* reqalts{"food": "caribbean"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-381a50592b-20130323_235612
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant"}
 - utter_request
* inform{"area": "north"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-e8997b10da-20130329_010926
* hello
 - utter_welcomemsg
* affirm{"pricerange": "expensive", "type": "restaurant", "area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-59bc8a2167-20130325_135337
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap"}
 - utter_request
* inform{"type": "restaurant"}
 - utter_request
* inform
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-e99e4f4538-20130328_203355
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform
 - utter_request
* inform{"food": "venetian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "mediterranean"}
 - utter_request
* inform{"pricerange": "expensive"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-583e7cede5-20130324_055306
* hello
 - utter_welcomemsg
* inform{"area": "south", "pricerange": "expensive", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-8f9fb7a86b-20130328_184504
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-10beae627f-20130401_164954
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform
 - utter_request
* inform
 - utter_request
* inform{"type": "restaurant", "task": "find"}
 - action_suggest
 - utter_canthelp
* reqalts{"type": "restaurant", "food": "gastropub"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* reqalts{"food": "gastropub"}
 - utter_expl-conf
* inform{"food": "gastropub"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-ddcaad92a1-20130325_234956
* hello
 - utter_welcomemsg
* hello{"food": "scandinavian", "task": "find"}
 - utter_request
* inform
 - utter_request
* inform{"food": "scandinavian"}
 - utter_request
* inform
 - utter_reqmore
* negate
 - utter_repeat
* inform{"type": "restaurant", "food": "scandinavian"}
 - utter_reqmore
* inform{"type": "restaurant"}
 - utter_reqmore
* negate
 - utter_repeat
* inform{"food": "scandinavian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "thai"}
 - action_suggest
 - utter_canthelp
* inform{"food": "thai"}
 - utter_expl-conf
* affirm
 - utter_expl-conf
* negate
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* inform{"food": "thai"}
 - action_suggest
 - utter_canthelp
* inform{"food": "thai"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_select
* inform
 - action_suggest
 - utter_select
* inform
 - action_suggest
 - utter_select
* inform{"food": "thai"}
 - action_suggest
 - utter_select
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-381a50592b-20130326_040539
* hello
 - utter_welcomemsg
* inform{"food": "danish"}
 - action_suggest
 - utter_canthelp
* inform{"food": "vietnamese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-78f497f314-20130323_184110
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-da4a08ad84-20130328_155120
* hello
 - utter_welcomemsg
* inform{"area": "east", "pricerange": "expensive", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-e54437a6f0-20130326_194636
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "area": "south"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-14f776f781-20130328_142356
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"food": "basque", "pricerange": "expensive", "type": "restaurant", "task": "find"}
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* reqalts{"food": "korean"}
 - action_suggest
 - utter_offer
* inform{"food": "korean"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "area"}
 - action_request
 - utter_offer
* bye

## story_voip-908884f5fd-20130326_224812
* hello
 - utter_welcomemsg
* inform{"area": "east", "type": "restaurant", "task": "find", "food": "belgian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-b08f15a787-20130402_070704
* hello
 - utter_welcomemsg
* inform{"food": "belgian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "portuguese"}
 - action_suggest
 - utter_canthelp
* inform{"food": "portuguese"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-d225fad9df-20130328_205151
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant", "area": "east"}
 - utter_request
* inform{"food": "north american"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-13ff413553-20130328_172109
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant"}
 - utter_request
* inform{"area": "north"}
 - utter_expl-conf
* negate{"area": "north"}
 - utter_request
* inform
 - utter_request
* inform{"food": "north american"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* inform

## story_voip-187c1708f2-20130325_131253
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "food": "catalan"}
 - action_suggest
 - utter_canthelp
* inform{"food": "spanish"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-43479eb5c2-20130329_045902
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform{"pricerange": "moderate", "type": "restaurant"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-0f41c16f2f-20130325_192310
* hello
 - utter_welcomemsg
* inform{"food": "german", "type": "restaurant", "task": "find"}
 - utter_expl-conf
* affirm
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_canthelp
* reqalts{"food": "french"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant", "food": "french"}
 - utter_expl-conf
* bye

## story_voip-e99e4f4538-20130328_195927
* hello
 - utter_welcomemsg
* inform{"type": "restaurant"}
 - utter_request
* inform{"area": "west"}
 - utter_request
* inform{"food": "indian"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-4b7e22cc07-20130401_185110
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "task": "find"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"food": "swedish"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "indian"}
 - action_suggest
 - utter_canthelp
* inform{"food": "indian"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-1b51204ef5-20130401_173145
* hello
 - utter_welcomemsg
* inform{"food": "indian"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform{"food": "indian"}
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_canthelp
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-e72dba1759-20130325_210629
* hello
 - utter_welcomemsg
* inform{"area": "north", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-13ff413553-20130328_174036
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate"}
 - utter_request
* inform{"area": "west"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-03c59ba692-20130325_180735
* hello
 - utter_welcomemsg
* inform{"pricerange": "moderate", "type": "restaurant", "area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "postcode"}
 - action_request
 - utter_offer
* bye

## story_voip-be5b7bf9d9-20130401_155552
* hello
 - utter_welcomemsg
* inform
 - utter_request
* inform
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* inform{"food": "vietnamese"}
 - action_suggest
 - utter_canthelp
* reqalts{"food": "vietnamese"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-922209b777-20130325_162603
* hello
 - utter_welcomemsg
* inform{"area": "east", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

## story_voip-b27a230d2e-20130323_053403
* hello
 - utter_welcomemsg
* inform{"area": "north", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* thankyou
 - action_suggest
 - utter_offer
* bye
 - utter_repeat
* bye

## story_voip-4f069a4136-20130327_211252
* hello
 - utter_welcomemsg
* inform{"pricerange": "cheap"}
 - utter_request
* inform{"area": "south"}
 - utter_request
* inform
 - utter_expl-conf
* affirm
 - action_suggest
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-03c2655d43-20130327_195546
* hello
 - utter_welcomemsg
* inform{"area": "west", "food": "creative"}
 - utter_expl-conf
* affirm{"food": "creative"}
 - action_suggest
 - utter_canthelp
* inform{"food": "italian"}
 - utter_expl-conf
* affirm{"area": "west"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-15d8a89cec-20130327_020852
* hello
 - utter_welcomemsg
* inform{"type": "restaurant", "area": "north", "food": "fusion"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant", "area": "north", "food": "asian oriental"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant", "area": "north"}
 - utter_expl-conf
* negate
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant", "food": "asian oriental"}
 - action_suggest
 - utter_canthelp
* restart
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant", "food": "asian oriental"}
 - utter_expl-conf
* affirm
 - utter_expl-conf
* negate
 - action_suggest
 - utter_canthelp
* inform
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant"}
 - action_suggest
 - utter_canthelp
* inform{"type": "restaurant"}
 - utter_expl-conf
* inform{"food": "asian oriental"}
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-e9b53d6ace-20130324_222855
* hello
 - utter_welcomemsg
* inform{"area": "west", "pricerange": "cheap", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "addr", "slot":  "phone"}
 - action_request
 - utter_offer
* bye

## story_voip-5749b16764-20130328_151234
* hello
 - utter_welcomemsg
* inform{"area": "west", "pricerange": "moderate", "type": "restaurant", "task": "find"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "addr"}
 - action_request
 - utter_offer
* bye

## story_voip-21ec2b7850-20130327_033947
* hello
 - utter_welcomemsg
* inform{"pricerange": "expensive", "type": "restaurant"}
 - utter_request
* inform{"area": "east"}
 - utter_request
* inform
 - action_suggest
 - utter_offer
* reqalts
 - action_suggest
 - utter_offer
* inform{"type": "restaurant"}
 - action_suggest
 - utter_offer
* inform{"type": "restaurant"}
 - action_suggest
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "phone"}
 - action_request
 - utter_offer
* request{"slot": "food"}
 - action_request
 - utter_offer
* bye

