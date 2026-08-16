# Prompting Guide

Use this guide after inspecting the model and garment images.

## Image Roles

Label inputs explicitly:

- Image 1: model reference, preserve identity and body.
- Image 2: garment reference, transfer garment faithfully.
- Additional images: optional style, pose, background, or accessory references only when the user says so.

If the user supplies a model already wearing a different outfit, replace only the outfit area needed for the requested garment. Preserve face, hair, pose family, body shape, hands, and camera angle.

## Master Prompt Template

```text
Use case: identity-preserve
Asset type: fashion virtual try-on batch image
Input images: Image 1 is the model reference; Image 2 is the garment reference.
Primary request: create one realistic fashion try-on image of the model wearing the supplied garment in [scene name], as part of a selected [1 / 4 / 9]-image output set.
Scene/backdrop: [scene description].
Subject: same model identity, face, body proportions, hair, skin tone, and natural presence from Image 1.
Garment: faithfully transfer the garment from Image 2, preserving silhouette, fabric, color, print, neckline, sleeves, hem, seams, fasteners, drape, texture, and fit.
Composition/framing: [3:4 portrait / 9:16 vertical / 1:1 square], [full body / three-quarter / seated / walking], fashion editorial/ecommerce crop with the garment clearly visible.
Lighting/mood: [scene lighting], realistic shadows and reflections matched to the environment.
Constraints: change only clothing and scene as needed; keep identity and anatomy plausible; garment must conform naturally to pose and perspective.
Avoid: extra people, duplicate limbs, changed face, changed body shape, generic replacement clothing, invented logos, text, watermark, UI overlay, distorted hands, broken seams, oversexualized styling, plastic skin, painterly look.
```

## Scene-Specific Lines

Add 1-3 lines per scene:

- "Place the model on a quiet city crosswalk at golden hour, mid-stride, with soft backlight and realistic street reflections."
- "Use a clean ecommerce studio with warm off-white sweep, full-body crop, neutral stance, and crisp garment detail."
- "Set the model near a resort pool under hard Mediterranean sunlight, with clean shadows and breezy editorial posture."
- "Use a moody hotel corridor at night with warm sconces and polished floor reflections, keeping the garment readable."

## Garment Fidelity Checklist

Name visible garment features in the prompt. Mention:

- item type: dress, coat, jacket, top, skirt, pants, set, gown, suit, etc.
- dominant color and secondary colors
- material: silk, denim, leather, wool, knit, chiffon, linen, sequins, etc.
- shape: oversized, fitted, A-line, cropped, floor-length, structured, draped
- key details: collar, lapel, cutout, buttons, zipper, pleats, slit, cuffs, waistband, pockets, print, embroidery

If unsure about a detail, describe only what is visible.

## Batch Variation Rules

Vary only what should vary:

- background scene
- lighting and time of day
- pose family within plausible identity preservation
- crop/framing
- camera lens feel

Keep stable:

- model identity
- garment design
- garment color/material/pattern
- fit logic and body proportions
- output polish level
- selected aspect ratio across the whole set unless the user asks to mix ratios

## Scene And Output Choice Rules

Before final image generation, confirm or infer:

- selected candidate scene number(s)
- image count: exactly `1`, `4`, or `9`
- aspect ratio: exactly `3:4`, `9:16`, or `1:1`

If the user has not selected these, ask a compact question in the user's language. Do not generate final images until the missing choices are known.

Use one image-generation call per final image. For 4 or 9 outputs, vary pose, crop, camera distance, lighting angle, or moment while preserving the same model identity and garment design.

## Corrective Prompt Examples

Use one concise correction if a scene fails:

```text
Regenerate the same scene. The previous result changed the garment design. Preserve the exact garment silhouette, color, texture, neckline, sleeves, hem, and visible seams from Image 2. Keep the model identity from Image 1 unchanged.
```

```text
Regenerate the same scene. The previous result distorted the hands and body proportions. Keep anatomy natural, hands simple and plausible, and keep the garment clearly visible.
```

```text
Regenerate the same scene. The previous result looked like a generic fashion ad. Remove all logos, text, overlays, and extra people. Keep a clean photoreal editorial image.
```
