from client import CinematicStoryboardSceneSequenceSynthesizerClient

def main():
    client = CinematicStoryboardSceneSequenceSynthesizerClient()
    res = client.synthesize_storyboard_scenes('Noir detective uncovering clandestine laboratory under torrential rain', 6)
    print('Storyboard Synthesizer: ' + res['storyboard_id'] + ' (' + str(res['shots_synthesized_count']) + ' shots)')
    print('Aspect Ratio: ' + res['aspect_ratio'] + ' | Continuity Score: ' + str(res['cinematography_continuity_score_pct']) + '%')
    print('Storyboard PDF: ' + res['rendered_storyboard_sheet_pdf_url'])

if __name__ == '__main__':
    main()
