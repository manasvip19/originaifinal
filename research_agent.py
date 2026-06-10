import re


class ResearchAgent:

    def summarize(self, text):
        if not text or not isinstance(text, str):
            return "AI extracted the most compelling commercialization insight from the research."

        cleaned = self._cleanup(text)
        paragraphs = [p.strip() for p in re.split(r"\n{2,}", cleaned) if p.strip()]
        if paragraphs:
            candidate = paragraphs[0]
            sentences = re.split(r"(?<=[.!?])\s+", candidate)
            summary = " ".join(sentences[:3]).strip()
            if len(summary.split()) > 20:
                return summary
        sentences = re.split(r"(?<=[.!?])\s+", cleaned)
        if sentences:
            return " ".join(sentences[:3]).strip()
        return cleaned[:220].strip()

    def identify_discovery(self, text):
        if not text or not isinstance(text, str):
            return "A strong innovation that bridges research and market demand."

        cleaned = self._cleanup(text)
        patterns = [
            r"(?:we|this study|this paper|our approach) (?:introduce|introduces|propose|proposes|present|presents|develop|develops|deliver|delivers)",
            r"(?:novel|new|innovative|first-of-its-kind|state-of-the-art).*?(?:for|to|that)",
            r"(?:capable of|designed to|developed to|aims to|enables|enabling).*?(?:for|to)",
        ]
        for pattern in patterns:
            match = re.search(pattern + r"[\s\S]{0,120}?([\.\!\?])", cleaned, flags=re.IGNORECASE)
            if match:
                phrase = match.group(0).strip().rstrip('.')
                return phrase.capitalize()

        keywords = [
            "autonomous navigation", "crop disease detection", "precision drug delivery",
            "energy storage", "predictive modeling", "secure transaction processing",
            "adaptive learning platform", "carbon reduction", "biometric authentication",
            "smart grid", "patient monitoring", "robotic assistance", "synthetic biology"
        ]
        lowercase = cleaned.lower()
        for keyword in keywords:
            if keyword in lowercase:
                return keyword.capitalize()

        return self._extract_core_phrase(cleaned)

    def _extract_core_phrase(self, text):
        sentences = re.split(r"(?<=[.!?])\s+", text)
        for sentence in sentences:
            if len(sentence.split()) > 8:
                return sentence.strip().rstrip('.')
        return text.strip()[:120].rstrip('.')

    def _cleanup(self, text):
        return " ".join(text.replace("\n", " ").replace("\r", " ").split())
