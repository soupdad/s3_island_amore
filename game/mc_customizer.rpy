init python:
    import random

    def customize_character(part, direction):
        global eye_brow
        global eye
        global nose
        global mouth
        global hair

        if direction == "right":
            if part == "eye_brow":
                if eye_brows.index(eye_brow) < len(eye_brows) - 1:
                    eye_brow = eye_brows[eye_brows.index(eye_brow) + 1]
                else:
                    eye_brow = eye_brows[0]
            if part == "eye":
                if eyes.index(eye) < len(eyes) - 1:
                    eye = eyes[eyes.index(eye) + 1]
                else:
                    eye = eyes[0]
            if part == "nose":
                if noses.index(nose) < len(noses) - 1:
                    nose = noses[noses.index(nose) + 1]
                else:
                    nose = noses[0]
            if part == "mouth":
                if mouths.index(mouth) < len(mouths) - 1:
                    mouth = mouths[mouths.index(mouth) + 1]
                else:
                    mouth = mouths[0]
            if part == "hair":
                if hairs.index(hair) < len(hairs) - 1:
                    hair = hairs[hairs.index(hair) + 1]
                else:
                    hair = hairs[0]
        elif direction == "left":
            if part == "eye_brow":
                if eye_brows.index(eye_brow) > 0:
                    eye_brow = eye_brows[eye_brows.index(eye_brow) - 1]
                else:
                    eye_brow = eye_brows[-1]
            if part == "eye":
                if eyes.index(eye) > 0:
                    eye = eyes[eyes.index(eye) - 1]
                else:
                    eye = eyes[-1]
            if part == "nose":
                if noses.index(nose) > 0:
                    nose = noses[noses.index(nose) - 1]
                else:
                    nose = noses[-1]
            if part == "mouth":
                if mouths.index(mouth) > 0:
                    mouth = mouths[mouths.index(mouth) - 1]
                else:
                    mouth = mouths[-1]
            if part == "hair":
                if hairs.index(hair) > 0:
                    hair = hairs[hairs.index(hair) - 1]
                else:
                    hair = hairs[-1]

        renpy.retain_after_load()

    # def customize_character(part, direction):
    #     global hair
    #     global eye

    #     if direction == "right":
    #         if part == "hair":
    #             if hairs.index(hair) < len(hairs) - 1:
    #                 hair = hairs[hairs.index(hair) + 1]
    #             else:
    #                 hair = hairs[0]
    #         if part == "eye":
    #             if eyes.index(eye) < len(eyes) - 1:
    #                 eye = eyes[eyes.index(eye) + 1]
    #             else:
    #                 eye = eyes[0]
    #     elif direction == "left":
    #         if part == "hair":
    #             if hairs.index(hair) > 0:
    #                 hair = hairs[hairs.index(hair) - 1]
    #             else:
    #                 hair = hairs[-1]
    #         if part == "eye":
    #             if eyes.index(eye) > 0:
    #                 eye = eyes[eyes.index(eye) - 1]
    #             else:
    #                 eye = eyes[-1]
            


    #     renpy.retain_after_load()

    def customize_colors(part, color):
        global hair_color
        global eye_color
        global body
        global mouth_color
        global mouth_color_other

        if part == "hair":
            hair_color = color
        elif part == "eyes":
            eye_color = color
        elif part == "body":
            body = color
        elif part == "mouth":
            mouth_color = color
            if color == "pink":
                mouth_color_other = "brown"
            else:
                mouth_color_other = "pink"

        renpy.retain_after_load()

    def customize_clothes(style, direction):
        global s3_mc_outfit
        global s3_mc_outfit_type

        if style == "swim":
            s3_mc_outfit_type = "swim_bikini"
            if direction == "right":
                if swim.index(s3_mc_outfit) < len(swim) - 1:
                    s3_mc_outfit = swim[swim.index(s3_mc_outfit) + 1]
                else:
                    s3_mc_outfit = swim[0]
            else:
                if swim.index(s3_mc_outfit) > 0:
                    s3_mc_outfit = swim[swim.index(s3_mc_outfit) - 1]
                else:
                    s3_mc_outfit = swim[-1]
        elif style == "evening":
            s3_mc_outfit_type = "party_dress"
            if direction == "right":
                if evening.index(s3_mc_outfit) < len(evening) - 1:
                    s3_mc_outfit = evening[evening.index(s3_mc_outfit) + 1]
                else:
                    s3_mc_outfit = evening[0]
            else:
                if evening.index(s3_mc_outfit) > 0:
                    s3_mc_outfit = evening[evening.index(s3_mc_outfit) - 1]
                else:
                    s3_mc_outfit = evening[-1]
        elif style == "pjs":
            s3_mc_outfit_type = "sleep_pajama"
            if direction == "right":
                if pjs.index(s3_mc_outfit) < len(pjs) - 1:
                    s3_mc_outfit = pjs[pjs.index(s3_mc_outfit) + 1]
                else:
                    s3_mc_outfit = pjs[0]
            else:
                if pjs.index(s3_mc_outfit) > 0:
                    s3_mc_outfit = pjs[pjs.index(s3_mc_outfit) - 1]
                else:
                    s3_mc_outfit = pjs[-1]
        
        renpy.retain_after_load()

    def randomize_style(part, style="none"):
        global eye_brow
        global eye
        global nose
        global mouth
        global hair
        global hair_color
        global eye_color
        global body
        global mouth_color
        global mouth_color_other
        global s3_mc_outfit
        global s3_mc_outfit_type

        if part == "look":
            # body
            body = bodies[random.randrange(0, len(bodies)-1)]
            # eyebrows
            eye_brow = eye_brows[random.randrange(0, len(eye_brows)-1)]
            # eyes
            eye = eyes[random.randrange(0, len(eyes)-1)]
            # eye color
            eye_color = eye_colors[random.randrange(0, len(eye_colors)-1)]
            # nose
            nose = noses[random.randrange(0, len(noses)-1)]
            # mouth
            mouth = mouths[random.randrange(0, len(mouths)-1)]
            # mouth_color
            mouth_color = mouth_colors[random.randrange(0, len(mouth_colors)-1)]
            if mouth_color == "pink":
                mouth_color_other = "brown"
            else:
                mouth_color_other = "pink"
            # hair
            hair = hairs[random.randrange(0, len(hairs)-1)]
            # hair_color
            hair_color = hair_colors[random.randrange(0, len(hair_colors)-1)]
        elif part == "clothes":
            if style == "swim":
                s3_mc_outfit_type = "swim_bikini"
                s3_mc_outfit = swim[random.randrange(0, len(swim)-1)]
            elif style == "evening":
                s3_mc_outfit_type = "party_dress"
                s3_mc_outfit = evening[random.randrange(0, len(evening)-1)]
            elif style == "pjs":
                s3_mc_outfit_type = "sleep_pajama"
                s3_mc_outfit = pjs[random.randrange(0, len(pjs)-1)]
