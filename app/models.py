import time
from django.db import models
from openai import OpenAI

class ModerationRecord(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    flagged = models.BooleanField(default=False)
    categories = models.JSONField()
    category_scores = models.JSONField()

    def __str__(self):
        return f'{self.flagged} | {self.content}'

class ModerationAttempt:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def get_results(self, message):
        max_retries = 5
        delay = 2  # seconds initial delay

        for attempt in range(max_retries):
            try:
                response = self.client.moderations.create(
                    model="omni-moderation-latest",
                    input=message,
                )

                if response and hasattr(response, 'results') and len(response.results) > 0:
                    results = response.results[0]

                    moderation = ModerationRecord.objects.create(
                        content=message,
                        flagged=results.flagged,
                        categories=results.categories,
                        category_scores=results.category_scores,
                    )
                    moderation.save()

                    results_dict = results.to_dict() if hasattr(results, "to_dict") else dict(results)
                    results_dict['id'] = moderation.id
                    return results_dict

                else:
                    raise Exception(f'Failed to receive results: {response}')

            except Exception as e:
                error_message = str(e).lower()
                if 'rate limit' in error_message or '429' in error_message:
                    if attempt < max_retries - 1:
                        sleep_time = delay * (2 ** attempt)
                        print(f"Rate limit hit, retrying in {sleep_time} seconds...")
                        time.sleep(sleep_time)
                        continue
                    else:
                        raise Exception("Rate limit exceeded after retries.") from e
                else:
                    raise
