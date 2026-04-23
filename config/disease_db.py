SEVERITY_COLORS = {
    "None":     ("#27ae60", "#1e8449"),
    "Moderate": ("#f39c12", "#d68910"),
    "High":     ("#e67e22", "#ca6f1e"),
    "Critical": ("#c0392b", "#a93226"),
    "Unknown":  ("#7f8c8d", "#717d7e"),
}

DISEASE_DB = {
    "Apple___Apple_scab": {
        "display": "Apple Scab", "plant": "Apple", "type": "Fungal",
        "severity": "Moderate", "emoji": "🍎", "color": "#e74c3c",
        "description": "Apple scab is caused by the fungus Venturia inaequalis. It produces dark, scabby lesions on leaves and fruit, reducing yield and market value.",
        "symptoms": ["Dark olive-green to black spots on leaves", "Velvety texture on lesions", "Yellowing and premature leaf drop", "Scabby, cracked spots on fruit"],
        "prevention": ["Apply fungicide sprays (captan, myclobutanil) from bud break", "Remove and destroy fallen infected leaves", "Prune trees to improve air circulation", "Plant resistant apple varieties"],
        "treatment": ["Spray with approved fungicides every 7–10 days during wet weather", "Use sulfur-based or copper-based sprays", "Avoid overhead irrigation"],
        "spread": "Wind and rain splash"
    },
    "Apple___Black_rot": {
        "display": "Apple Black Rot", "plant": "Apple", "type": "Fungal",
        "severity": "High", "emoji": "🍎", "color": "#c0392b",
        "description": "Black rot is caused by Botryosphaeria obtusa. It affects fruit, leaves, and bark, causing significant losses if untreated.",
        "symptoms": ["Purple spots on leaves with brown centers", "Black rotted areas on fruit", "Cankers on branches", "Fruit mummification"],
        "prevention": ["Prune out dead or cankered wood", "Remove mummified fruit from trees and ground", "Avoid wounding trees", "Apply fungicide during growing season"],
        "treatment": ["Apply fungicides containing thiophanate-methyl or captan", "Remove infected plant material immediately", "Maintain tree vigor with proper nutrition"],
        "spread": "Rain, wind, infected wood"
    },
    "Apple___Cedar_apple_rust": {
        "display": "Cedar Apple Rust", "plant": "Apple", "type": "Fungal",
        "severity": "Moderate", "emoji": "🍎", "color": "#e67e22",
        "description": "Cedar apple rust requires two hosts — cedar/juniper and apple. It causes orange-yellow spots on apple leaves and fruit.",
        "symptoms": ["Bright orange-yellow spots on upper leaf surface", "Orange spore tubes on lower leaf surface", "Deformed or spotted fruit", "Premature defoliation"],
        "prevention": ["Remove nearby cedar/juniper trees if possible", "Plant rust-resistant apple varieties", "Apply fungicides at early season"],
        "treatment": ["Myclobutanil or trifloxystrobin fungicide sprays", "Begin spraying at pink bud stage", "Continue every 7–10 days through petal fall"],
        "spread": "Wind-borne spores from cedar trees"
    },
    "Apple___healthy": {
        "display": "Healthy Apple Leaf", "plant": "Apple", "type": "Healthy",
        "severity": "None", "emoji": "🍎", "color": "#27ae60",
        "description": "The apple leaf is healthy with no signs of disease or infection.",
        "symptoms": ["No visible disease symptoms"],
        "prevention": ["Maintain regular pruning schedule", "Monitor periodically for early signs of disease", "Ensure proper nutrition and irrigation"],
        "treatment": ["No treatment needed — keep up the great care!"],
        "spread": "N/A"
    },
    "Blueberry___healthy": {
        "display": "Healthy Blueberry Leaf", "plant": "Blueberry", "type": "Healthy",
        "severity": "None", "emoji": "🫐", "color": "#27ae60",
        "description": "The blueberry plant appears healthy with no visible disease symptoms.",
        "symptoms": ["No visible disease symptoms"],
        "prevention": ["Ensure acidic well-drained soil (pH 4.5–5.5)", "Regular mulching and adequate irrigation"],
        "treatment": ["No treatment needed"],
        "spread": "N/A"
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "display": "Cherry Powdery Mildew", "plant": "Cherry", "type": "Fungal",
        "severity": "Moderate", "emoji": "🍒", "color": "#9b59b6",
        "description": "Caused by Podosphaera clandestina. A white powdery coating appears on leaves and shoots, stunting growth.",
        "symptoms": ["White powdery coating on leaves", "Distorted, curling young leaves", "Stunted shoot growth", "Reduced fruit quality"],
        "prevention": ["Ensure good air circulation through pruning", "Avoid excessive nitrogen fertilization", "Plant resistant varieties"],
        "treatment": ["Sulfur or potassium bicarbonate sprays", "Apply neem oil as an organic option", "Use systemic fungicides like myclobutanil"],
        "spread": "Wind-dispersed spores"
    },
    "Cherry_(including_sour)___healthy": {
        "display": "Healthy Cherry Leaf", "plant": "Cherry", "type": "Healthy",
        "severity": "None", "emoji": "🍒", "color": "#27ae60",
        "description": "The cherry leaf is healthy with no signs of disease.",
        "symptoms": ["No visible disease symptoms"],
        "prevention": ["Regular monitoring and proper pruning"],
        "treatment": ["No treatment needed"],
        "spread": "N/A"
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "display": "Corn Gray Leaf Spot", "plant": "Corn (Maize)", "type": "Fungal",
        "severity": "High", "emoji": "🌽", "color": "#95a5a6",
        "description": "Caused by Cercospora zeae-maydis. One of the most significant foliar diseases of corn, causing rectangular gray lesions.",
        "symptoms": ["Rectangular, grayish-tan lesions on leaves", "Lesions run parallel to leaf veins", "Premature leaf death", "Yield reduction up to 50%"],
        "prevention": ["Rotate crops — avoid continuous corn planting", "Use resistant hybrids", "Manage crop residue by tilling"],
        "treatment": ["Foliar fungicides (strobilurins, triazoles) at silking stage", "Apply when disease is first detected", "Scout fields regularly"],
        "spread": "Wind, rain splash from residue"
    },
    "Corn_(maize)___Common_rust_": {
        "display": "Corn Common Rust", "plant": "Corn (Maize)", "type": "Fungal",
        "severity": "Moderate", "emoji": "🌽", "color": "#e67e22",
        "description": "Caused by Puccinia sorghi. Common rust produces brick-red pustules on both leaf surfaces.",
        "symptoms": ["Brick-red to brown oval pustules on leaves", "Pustules on both upper and lower surfaces", "Yellowing and leaf death in severe cases"],
        "prevention": ["Plant rust-resistant corn hybrids", "Early planting to avoid peak spore periods"],
        "treatment": ["Fungicide applications (triazoles, strobilurins) if severe", "Most modern hybrids have adequate resistance"],
        "spread": "Wind-blown urediniospores"
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "display": "Corn Northern Leaf Blight", "plant": "Corn (Maize)", "type": "Fungal",
        "severity": "High", "emoji": "🌽", "color": "#c0392b",
        "description": "Caused by Exserohilum turcicum. Creates large, cigar-shaped grayish lesions that can destroy significant leaf area.",
        "symptoms": ["Large, cigar-shaped tan/gray lesions (1–6 inches)", "Dark green, water-soaked borders initially", "Blighting of entire leaves", "Green ears on dead plants"],
        "prevention": ["Plant resistant hybrids", "Crop rotation with non-host crops", "Manage crop debris"],
        "treatment": ["Foliar fungicides at tasseling if disease is severe", "Propiconazole or azoxystrobin-based fungicides"],
        "spread": "Wind and rain"
    },
    "Corn_(maize)___healthy": {
        "display": "Healthy Corn Leaf", "plant": "Corn (Maize)", "type": "Healthy",
        "severity": "None", "emoji": "🌽", "color": "#27ae60",
        "description": "The corn plant is healthy with no disease symptoms.",
        "symptoms": ["No visible disease symptoms"],
        "prevention": ["Balanced fertilization, crop rotation, and pest monitoring"],
        "treatment": ["No treatment needed"],
        "spread": "N/A"
    },
    "Grape___Black_rot": {
        "display": "Grape Black Rot", "plant": "Grape", "type": "Fungal",
        "severity": "High", "emoji": "🍇", "color": "#8e44ad",
        "description": "Caused by Guignardia bidwellii. One of the most destructive grape diseases, destroying entire fruit clusters.",
        "symptoms": ["Tan-brown spots with dark borders on leaves", "Brown mummified shriveled fruit", "Black lesions on shoots and tendrils"],
        "prevention": ["Remove mummified fruit and infected canes during dormancy", "Apply fungicides from bud break", "Ensure good air circulation through canopy management"],
        "treatment": ["Captan, myclobutanil, or mancozeb fungicide sprays", "Begin at budbreak, continue through fruit development"],
        "spread": "Rain splash from mummified fruit"
    },
    "Grape___Esca_(Black_Measles)": {
        "display": "Grape Esca (Black Measles)", "plant": "Grape", "type": "Fungal",
        "severity": "High", "emoji": "🍇", "color": "#6c3483",
        "description": "A complex trunk disease caused by several fungi. It causes tiger-striped leaves and measle-like spots on berries.",
        "symptoms": ["Tiger-striped discoloration on leaves (yellow/red borders)", "Dark spots on berries giving a measled appearance", "Wilting and shoot dieback", "Internal wood discoloration"],
        "prevention": ["Avoid large pruning wounds; use wound sealants", "Remove and destroy infected wood", "Sanitize pruning tools"],
        "treatment": ["No effective chemical cure exists", "Preventive sodium arsenite (banned in many regions)", "Remove heavily infected vines"],
        "spread": "Through pruning wounds"
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "display": "Grape Leaf Blight", "plant": "Grape", "type": "Fungal",
        "severity": "Moderate", "emoji": "🍇", "color": "#a93226",
        "description": "Caused by Pseudocercospora vitis. Creates angular brown spots on leaves, leading to early defoliation.",
        "symptoms": ["Angular dark-brown spots on upper leaf surface", "Gray sporulation on lower leaf surface", "Yellowing and premature leaf drop"],
        "prevention": ["Avoid excessive moisture; improve drainage", "Apply protective fungicides", "Remove infected leaves"],
        "treatment": ["Copper-based or mancozeb fungicides", "Improve canopy airflow through pruning"],
        "spread": "Wind and rain"
    },
    "Grape___healthy": {
        "display": "Healthy Grape Leaf", "plant": "Grape", "type": "Healthy",
        "severity": "None", "emoji": "🍇", "color": "#27ae60",
        "description": "The grape vine leaf is healthy with no visible signs of disease.",
        "symptoms": ["No visible disease symptoms"],
        "prevention": ["Regular canopy management and balanced fertilization"],
        "treatment": ["No treatment needed"],
        "spread": "N/A"
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "display": "Citrus Greening (HLB)", "plant": "Orange", "type": "Bacterial",
        "severity": "Critical", "emoji": "🍊", "color": "#c0392b",
        "description": "Caused by Candidatus Liberibacter. The most devastating citrus disease worldwide, currently has no cure.",
        "symptoms": ["Asymmetric blotchy mottling of leaves (yellowing)", "Stunted misshapen fruit with bitter taste", "Green fruit that fails to color properly", "Twig and branch dieback"],
        "prevention": ["Use certified disease-free nursery trees", "Control the Asian citrus psyllid vector with insecticides", "Remove and destroy infected trees immediately"],
        "treatment": ["No cure exists — infected trees must be removed", "Control psyllid populations to prevent spread", "Nutritional sprays may extend tree life temporarily"],
        "spread": "Asian citrus psyllid insect vector"
    },
    "Peach___Bacterial_spot": {
        "display": "Peach Bacterial Spot", "plant": "Peach", "type": "Bacterial",
        "severity": "High", "emoji": "🍑", "color": "#e74c3c",
        "description": "Caused by Xanthomonas arboricola pv. pruni. Affects leaves, twigs, and fruit of peaches and nectarines.",
        "symptoms": ["Small, angular water-soaked spots on leaves", "Spots turn purple-brown with yellow halos", "Defoliation in severe cases", "Sunken pits and cracks on fruit"],
        "prevention": ["Plant resistant varieties", "Avoid overhead irrigation", "Prune to improve air circulation"],
        "treatment": ["Copper-based bactericide sprays from budbreak", "Oxytetracycline sprays during bloom", "Multiple applications needed in wet seasons"],
        "spread": "Rain splash and wind"
    },
    "Peach___healthy": {
        "display": "Healthy Peach Leaf", "plant": "Peach", "type": "Healthy",
        "severity": "None", "emoji": "🍑", "color": "#27ae60",
        "description": "The peach tree leaf is healthy with no disease symptoms.",
        "symptoms": ["No visible disease symptoms"],
        "prevention": ["Regular pruning and proper nutrition"],
        "treatment": ["No treatment needed"],
        "spread": "N/A"
    },
    "Pepper,_bell___Bacterial_spot": {
        "display": "Bell Pepper Bacterial Spot", "plant": "Bell Pepper", "type": "Bacterial",
        "severity": "High", "emoji": "🫑", "color": "#e74c3c",
        "description": "Caused by Xanthomonas campestris. A major disease of peppers causing leaf and fruit spotting.",
        "symptoms": ["Small, water-soaked spots on leaves turning brown", "Yellow halos around lesions", "Premature defoliation", "Raised, scab-like lesions on fruit"],
        "prevention": ["Use certified disease-free seed", "Avoid overhead irrigation", "Practice crop rotation for 2–3 years"],
        "treatment": ["Copper-based bactericide sprays", "Applications every 5–7 days in wet weather", "Remove severely infected plants"],
        "spread": "Rain splash, contaminated seed"
    },
    "Pepper,_bell___healthy": {
        "display": "Healthy Bell Pepper Leaf", "plant": "Bell Pepper", "type": "Healthy",
        "severity": "None", "emoji": "🫑", "color": "#27ae60",
        "description": "The pepper plant is healthy with no visible disease signs.",
        "symptoms": ["No visible disease symptoms"],
        "prevention": ["Balanced fertilization and proper spacing for air flow"],
        "treatment": ["No treatment needed"],
        "spread": "N/A"
    },
    "Potato___Early_blight": {
        "display": "Potato Early Blight", "plant": "Potato", "type": "Fungal",
        "severity": "Moderate", "emoji": "🥔", "color": "#e67e22",
        "description": "Caused by Alternaria solani. A common foliar disease that reduces tuber yield and quality.",
        "symptoms": ["Dark brown circular spots with concentric rings (target-board pattern)", "Yellow halo around lesions", "Lower leaves affected first", "Premature leaf senescence"],
        "prevention": ["Crop rotation (at least 3 years)", "Use certified disease-free seed potatoes", "Balanced fertilization — avoid nitrogen stress"],
        "treatment": ["Fungicide sprays (chlorothalonil, mancozeb, azoxystrobin)", "Apply preventively before symptoms appear", "Remove and destroy infected debris"],
        "spread": "Wind, rain, and infected debris"
    },
    "Potato___Late_blight": {
        "display": "Potato Late Blight", "plant": "Potato", "type": "Oomycete",
        "severity": "Critical", "emoji": "🥔", "color": "#c0392b",
        "description": "Caused by Phytophthora infestans. The infamous cause of the Irish Potato Famine. Can destroy crops in days.",
        "symptoms": ["Pale green or brown water-soaked spots on leaves", "White fluffy sporulation on leaf undersides", "Rapidly spreading brown rot", "Foul-smelling tuber rot"],
        "prevention": ["Use certified disease-free seed", "Plant resistant varieties", "Avoid overhead irrigation and waterlogged soil"],
        "treatment": ["Fungicides: metalaxyl + mancozeb, or cymoxanil", "Apply preventively — curative action is limited", "Destroy infected plant material immediately"],
        "spread": "Wind-blown spores, very rapid"
    },
    "Potato___healthy": {
        "display": "Healthy Potato Leaf", "plant": "Potato", "type": "Healthy",
        "severity": "None", "emoji": "🥔", "color": "#27ae60",
        "description": "The potato plant is healthy with no signs of disease.",
        "symptoms": ["No visible disease symptoms"],
        "prevention": ["Crop rotation and use certified seed potatoes"],
        "treatment": ["No treatment needed"],
        "spread": "N/A"
    },
    "Raspberry___healthy": {
        "display": "Healthy Raspberry Leaf", "plant": "Raspberry", "type": "Healthy",
        "severity": "None", "emoji": "🫐", "color": "#27ae60",
        "description": "The raspberry plant shows no signs of disease and is in good health.",
        "symptoms": ["No visible disease symptoms"],
        "prevention": ["Ensure good drainage and sun exposure"],
        "treatment": ["No treatment needed"],
        "spread": "N/A"
    },
    "Soybean___healthy": {
        "display": "Healthy Soybean Leaf", "plant": "Soybean", "type": "Healthy",
        "severity": "None", "emoji": "🌿", "color": "#27ae60",
        "description": "The soybean plant is healthy with no disease symptoms.",
        "symptoms": ["No visible disease symptoms"],
        "prevention": ["Crop rotation and proper field scouting"],
        "treatment": ["No treatment needed"],
        "spread": "N/A"
    },
    "Squash___Powdery_mildew": {
        "display": "Squash Powdery Mildew", "plant": "Squash", "type": "Fungal",
        "severity": "Moderate", "emoji": "🎃", "color": "#9b59b6",
        "description": "Caused by Podosphaera xanthii or Erysiphe cichoracearum. Very common cucurbit disease that weakens plants.",
        "symptoms": ["White powdery coating on leaf surfaces", "Yellowing and browning of affected leaves", "Stunted plant growth", "Reduced fruit yield"],
        "prevention": ["Plant resistant varieties", "Avoid overhead watering", "Space plants for good air circulation"],
        "treatment": ["Potassium bicarbonate or sulfur sprays", "Neem oil as organic option", "Remove severely affected leaves"],
        "spread": "Wind-dispersed spores, thrives in dry weather"
    },
    "Strawberry___Leaf_scorch": {
        "display": "Strawberry Leaf Scorch", "plant": "Strawberry", "type": "Fungal",
        "severity": "Moderate", "emoji": "🍓", "color": "#e74c3c",
        "description": "Caused by Diplocarpon earlianum. Creates small purple spots that merge, giving leaves a scorched appearance.",
        "symptoms": ["Small, irregular purple or dark-red spots on leaves", "White to tan centers as lesions expand", "Browning and scorched appearance of leaves", "Reduced plant vigor and yield"],
        "prevention": ["Remove and destroy infected leaves", "Avoid overhead irrigation", "Use disease-free planting material"],
        "treatment": ["Captan or copper-based fungicide sprays", "Apply during early season before symptoms appear"],
        "spread": "Rain splash and wind"
    },
    "Strawberry___healthy": {
        "display": "Healthy Strawberry Leaf", "plant": "Strawberry", "type": "Healthy",
        "severity": "None", "emoji": "🍓", "color": "#27ae60",
        "description": "The strawberry plant is healthy with no visible disease.",
        "symptoms": ["No visible disease symptoms"],
        "prevention": ["Regular monitoring and proper bed management"],
        "treatment": ["No treatment needed"],
        "spread": "N/A"
    },
    "Tomato___Bacterial_spot": {
        "display": "Tomato Bacterial Spot", "plant": "Tomato", "type": "Bacterial",
        "severity": "High", "emoji": "🍅", "color": "#e74c3c",
        "description": "Caused by Xanthomonas species. A major tomato disease causing spotted leaves and fruit, reducing marketability.",
        "symptoms": ["Small, water-soaked spots on leaves turning dark brown", "Yellow halos around lesions", "Defoliation under severe infection", "Raised scab-like lesions on fruit surface"],
        "prevention": ["Use certified disease-free seed and transplants", "Avoid overhead irrigation", "Crop rotation for 2–3 years"],
        "treatment": ["Copper-based bactericide + mancozeb tank mix", "Apply every 5–7 days during wet weather", "Remove infected plant debris"],
        "spread": "Rain splash, wind, contaminated tools"
    },
    "Tomato___Early_blight": {
        "display": "Tomato Early Blight", "plant": "Tomato", "type": "Fungal",
        "severity": "Moderate", "emoji": "🍅", "color": "#e67e22",
        "description": "Caused by Alternaria solani. One of the most common tomato diseases, affecting lower leaves first.",
        "symptoms": ["Dark brown spots with concentric target-like rings", "Yellow halo surrounding lesions", "Lower/older leaves affected first", "Stem lesions (collar rot) in seedlings"],
        "prevention": ["Crop rotation (3-year cycle)", "Remove infected lower leaves early", "Avoid wetting foliage when watering"],
        "treatment": ["Chlorothalonil, mancozeb, or azoxystrobin fungicides", "Apply every 7–10 days, especially in humid weather", "Stake plants to improve airflow"],
        "spread": "Wind, rain, infected soil debris"
    },
    "Tomato___Late_blight": {
        "display": "Tomato Late Blight", "plant": "Tomato", "type": "Oomycete",
        "severity": "Critical", "emoji": "🍅", "color": "#c0392b",
        "description": "Caused by Phytophthora infestans. Can devastate tomato crops within days under cool, wet conditions.",
        "symptoms": ["Large, irregular dark-green to brown water-soaked lesions", "White mold growth on leaf undersides in humid conditions", "Rapid browning and collapse of tissue", "Brown rot of stems and fruit"],
        "prevention": ["Use resistant varieties", "Avoid planting near potatoes", "Do not work in fields when wet"],
        "treatment": ["Metalaxyl + mancozeb fungicide combination", "Apply preventively in cool/wet weather", "Destroy affected plant material immediately — do not compost"],
        "spread": "Wind-blown spores, extremely rapid spread"
    },
    "Tomato___Leaf_Mold": {
        "display": "Tomato Leaf Mold", "plant": "Tomato", "type": "Fungal",
        "severity": "Moderate", "emoji": "🍅", "color": "#8e44ad",
        "description": "Caused by Passalora fulva (Fulvia fulva). Primarily affects greenhouse tomatoes in high humidity environments.",
        "symptoms": ["Pale green-yellow spots on upper leaf surface", "Olive-green to brown velvety sporulation beneath", "Leaves curl upward, then wither", "Rarely affects fruit directly"],
        "prevention": ["Reduce humidity to below 85%", "Improve greenhouse ventilation", "Space plants adequately", "Use resistant varieties"],
        "treatment": ["Chlorothalonil or mancozeb-based fungicides", "Remove and destroy infected leaves", "Reduce humidity as a primary control"],
        "spread": "Airborne conidia, favored by high humidity"
    },
    "Tomato___Septoria_leaf_spot": {
        "display": "Tomato Septoria Leaf Spot", "plant": "Tomato", "type": "Fungal",
        "severity": "Moderate", "emoji": "🍅", "color": "#e67e22",
        "description": "Caused by Septoria lycopersici. Very common in wet seasons, causing rapid defoliation from lower leaves upward.",
        "symptoms": ["Numerous small circular spots with dark borders and gray centers", "Tiny black dots (pycnidia) visible in lesion centers", "Rapid defoliation starting from bottom", "Weakened plants with poor yield"],
        "prevention": ["Crop rotation (3 years)", "Stake and mulch plants", "Avoid wetting foliage", "Remove infected lower leaves promptly"],
        "treatment": ["Chlorothalonil, mancozeb, or copper-based fungicides", "Apply every 7–10 days during wet weather"],
        "spread": "Rain splash, soilborne inoculum"
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "display": "Tomato Spider Mites", "plant": "Tomato", "type": "Pest (Arachnid)",
        "severity": "High", "emoji": "🍅", "color": "#e74c3c",
        "description": "Two-spotted spider mites (Tetranychus urticae) are tiny arachnids that suck plant sap, causing stippling damage.",
        "symptoms": ["Tiny yellow or bronze stippling on leaf surface", "Fine webbing on undersides of leaves", "Leaves turn bronze, yellow, or brown", "Leaf drop in severe infestations"],
        "prevention": ["Maintain adequate soil moisture", "Avoid excessive nitrogen fertilizer", "Encourage natural predators (ladybugs, predatory mites)"],
        "treatment": ["Miticide sprays (abamectin, bifenazate)", "Neem oil or insecticidal soap for organic control", "Strong water sprays to dislodge mites", "Avoid broad-spectrum insecticides that kill predators"],
        "spread": "Wind, infested transplants, human activity"
    },
    "Tomato___Target_Spot": {
        "display": "Tomato Target Spot", "plant": "Tomato", "type": "Fungal",
        "severity": "Moderate", "emoji": "🍅", "color": "#c0392b",
        "description": "Caused by Corynespora cassiicola. Creates distinctive concentric target-like lesions across all above-ground plant parts.",
        "symptoms": ["Brown spots with concentric rings resembling a target", "Yellow halo around spots", "Lesions on leaves, stems, and fruit", "Severe defoliation in humid conditions"],
        "prevention": ["Crop rotation and field sanitation", "Stake plants for air circulation", "Avoid overhead irrigation"],
        "treatment": ["Chlorothalonil, azoxystrobin, or difenoconazole", "Begin spray program early in season"],
        "spread": "Airborne spores, rain splash"
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "display": "Tomato Yellow Leaf Curl Virus", "plant": "Tomato", "type": "Viral",
        "severity": "Critical", "emoji": "🍅", "color": "#c0392b",
        "description": "Caused by TYLCV, transmitted by whiteflies. Can cause complete crop loss if plants are infected young.",
        "symptoms": ["Upward curling and cupping of young leaves", "Yellowing (chlorosis) of leaf margins", "Stunted plant growth", "Flower drop and severe yield loss"],
        "prevention": ["Use TYLCV-resistant tomato varieties", "Control whitefly populations with reflective mulches and insecticides", "Use insect-proof net houses", "Remove and destroy infected plants early"],
        "treatment": ["No cure — remove infected plants to reduce spread", "Control whitefly vectors with imidacloprid or thiamethoxam", "Systemic insecticides as a preventive measure"],
        "spread": "Bemisia tabaci (silverleaf whitefly)"
    },
    "Tomato___Tomato_mosaic_virus": {
        "display": "Tomato Mosaic Virus", "plant": "Tomato", "type": "Viral",
        "severity": "High", "emoji": "🍅", "color": "#e74c3c",
        "description": "Caused by Tomato mosaic virus (ToMV). A highly stable virus that persists in soil and on tools for years.",
        "symptoms": ["Mosaic pattern of light and dark green on leaves", "Leaf distortion and curling", "Stunted growth and reduced fruit set", "Fruit shows internal browning or discoloration"],
        "prevention": ["Use certified virus-free seed or resistant varieties", "Sanitize hands and tools with 10% bleach solution", "Control aphid vectors", "Remove infected plants immediately"],
        "treatment": ["No chemical cure available", "Remove and destroy infected plants", "Strict sanitation of tools and hands"],
        "spread": "Contact (hands, tools), seed transmission, aphids"
    },
    "Tomato___healthy": {
        "display": "Healthy Tomato Leaf", "plant": "Tomato", "type": "Healthy",
        "severity": "None", "emoji": "🍅", "color": "#27ae60",
        "description": "The tomato plant is healthy with no signs of disease, pests, or viral infection.",
        "symptoms": ["No visible disease symptoms"],
        "prevention": ["Regular monitoring, proper watering, and balanced fertilization"],
        "treatment": ["No treatment needed — excellent plant health!"],
        "spread": "N/A"
    }
}
