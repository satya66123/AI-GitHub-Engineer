from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient


class LicenseAnalyzer:

    def __init__(self):

        self.ollama = OllamaClient()
        self.openai = OpenAIClient()

    # ----------------------------------------------------
    # AI Provider
    # ----------------------------------------------------

    def _generate(
        self,
        provider,
        model,
        prompt,
    ):

        if provider == AIProvider.OPENAI.value:

            return self.openai.generate(
                prompt=prompt,
                model=model,
            )

        return self.ollama.generate(
            prompt=prompt,
            model=model,
        )

    # ----------------------------------------------------
    # License Analysis
    # ----------------------------------------------------

    def analyze_license(
        self,
        provider,
        model,
        repository,
        license_text,
    ):

        prompt = f"""
You are an Open Source Compliance Expert.

Analyze the following software license.

Repository

{repository}

License

{license_text}

Generate

License Summary

License Type

Permissions

Conditions

Limitations

Commercial Usage

Patent Rights

Distribution Rules

Recommendations

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Dependency License Review
    # ----------------------------------------------------

    def dependency_review(
        self,
        provider,
        model,
        dependencies,
    ):

        prompt = f"""
Analyze dependency licenses.

Dependencies

{dependencies}

Generate

License Compatibility

Potential Conflicts

Commercial Usage Risks

Recommendations

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Compliance Report
    # ----------------------------------------------------

    def compliance_report(
        self,
        provider,
        model,
        repository,
        repository_information,
    ):

        prompt = f"""
Generate an Open Source Compliance Report.

Repository

{repository}

Repository Information

{repository_information}

Evaluate

License Compliance

Dependency Compliance

Attribution

Distribution

Commercial Readiness

Risk Assessment

Overall Score

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # License Compatibility
    # ----------------------------------------------------

    def compatibility_check(
        self,
        provider,
        model,
        primary_license,
        secondary_license,
    ):

        prompt = f"""
Compare two software licenses.

Primary License

{primary_license}

Secondary License

{secondary_license}

Explain

Compatibility

Conflicts

Distribution Impact

Commercial Impact

Recommendations

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Commercial Readiness
    # ----------------------------------------------------

    def commercial_review(
        self,
        provider,
        model,
        repository,
        license_text,
    ):

        prompt = f"""
Evaluate commercial usage readiness.

Repository

{repository}

License

{license_text}

Analyze

Commercial Usage

Redistribution

Patent Risks

Trademark Considerations

Recommendations

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # AI Recommendation
    # ----------------------------------------------------

    def recommend_license(
        self,
        provider,
        model,
        project_description,
    ):

        prompt = f"""
Recommend the best open-source license.

Project Description

{project_description}

Recommend

MIT

Apache 2.0

GPL

BSD

MPL

Explain

Advantages

Disadvantages

Commercial Suitability

Community Adoption

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )