#!/usr/bin/env python3
"""
Weak Signal Classification and Analysis
Based on The Tautai Principle

This script provides frameworks for classifying, prioritizing, and analyzing
weak signals detected in the organizational environment.

Key Framework Integration:
- Cynefin Framework: Contextual response patterns (Complex → Probe-Sense-Respond)
- OODA Loop: Signals feed the Observe phase, enabling faster competitive cycles
- Narrative Output: Transform signals into compelling stories, not just data
- Viability Focus: Assess impact on Adaptability, Resilience, Robustness, Excellence

The goal is not classification for its own sake, but building narratives that
accelerate sensemaking and drive adaptive action faster than competitors.
"""

from enum import Enum
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import json


class SignalType(Enum):
    """Types of weak signals based on their nature."""
    TECHNOLOGICAL = "technological"
    SOCIAL = "social"
    ECONOMIC = "economic"
    ENVIRONMENTAL = "environmental"
    POLITICAL = "political"
    COMPETITIVE = "competitive"
    REGULATORY = "regulatory"
    CONSUMER = "consumer"


class SignalStrength(Enum):
    """Signal strength classification."""
    VERY_WEAK = 1    # Barely perceptible, single source
    WEAK = 2         # Multiple mentions, still ambiguous
    EMERGING = 3     # Clear pattern, limited scope
    MODERATE = 4     # Widespread recognition, clear implications
    STRONG = 5       # Undeniable trend, immediate action needed


class TimeHorizon(Enum):
    """Expected time horizon for signal impact."""
    IMMEDIATE = "0-1 years"
    SHORT_TERM = "1-3 years"
    MEDIUM_TERM = "3-5 years"
    LONG_TERM = "5-10 years"
    VERY_LONG_TERM = "10+ years"


class CynefinDomain(Enum):
    """Cynefin domains for contextual response patterns."""
    CLEAR = "clear"           # Known knowns, best practices
    COMPLICATED = "complicated"  # Known unknowns, expert analysis
    COMPLEX = "complex"       # Unknown unknowns, experiments (most weak signals)
    CHAOTIC = "chaotic"       # Crisis, immediate action
    CONFUSED = "confused"     # Domain unclear, needs assessment


class ResponsePattern(Enum):
    """Recommended response patterns based on Cynefin domain."""
    SENSE_CATEGORIZE_RESPOND = "sense_categorize_respond"  # Clear
    SENSE_ANALYZE_RESPOND = "sense_analyze_respond"        # Complicated
    PROBE_SENSE_RESPOND = "probe_sense_respond"            # Complex (default for weak signals)
    ACT_SENSE_RESPOND = "act_sense_respond"                # Chaotic


class WeakSignal:
    """Structured representation of a weak signal."""
    
    def __init__(self,
                 title: str,
                 description: str,
                 signal_type: SignalType,
                 sources: List[str],
                 first_observed: str,
                 observer: str):
        self.id = self._generate_id()
        self.title = title
        self.description = description
        self.signal_type = signal_type
        self.sources = sources
        self.first_observed = first_observed
        self.observer = observer
        self.strength = self._assess_initial_strength()
        self.cynefin_domain = CynefinDomain.COMPLEX  # Default for weak signals
        self.response_pattern = ResponsePattern.PROBE_SENSE_RESPOND
        self.potential_impact = None
        self.uncertainty_level = None
        self.time_horizon = None
        self.related_signals = []
        self.narrative = None  # Compelling story about the signal
        self.viability_impact = {  # Impact on four pillars
            "adaptability": None,
            "resilience": None,
            "robustness": None,
            "operational_excellence": None
        }
        self.status = "new"
        self.last_updated = datetime.now().isoformat()
        
    def _generate_id(self) -> str:
        """Generate unique signal ID."""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"WS-{timestamp}"
    
    def _assess_initial_strength(self) -> SignalStrength:
        """Assess initial signal strength based on sources."""
        if len(self.sources) == 1:
            return SignalStrength.VERY_WEAK
        elif len(self.sources) <= 3:
            return SignalStrength.WEAK
        else:
            return SignalStrength.EMERGING
    
    def to_dict(self) -> Dict:
        """Convert signal to dictionary format."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "signal_type": self.signal_type.value,
            "sources": self.sources,
            "first_observed": self.first_observed,
            "observer": self.observer,
            "strength": self.strength.value,
            "cynefin_domain": self.cynefin_domain.value,
            "response_pattern": self.response_pattern.value,
            "potential_impact": self.potential_impact,
            "uncertainty_level": self.uncertainty_level,
            "time_horizon": self.time_horizon.value if self.time_horizon else None,
            "related_signals": self.related_signals,
            "narrative": self.narrative,
            "viability_impact": self.viability_impact,
            "status": self.status,
            "last_updated": self.last_updated
        }


class SignalAnalyzer:
    """Framework for analyzing and prioritizing weak signals."""
    
    IMPACT_CRITERIA = {
        "strategic_relevance": {
            "weight": 0.20,
            "description": "Alignment with strategic objectives and core business"
        },
        "disruptive_potential": {
            "weight": 0.20,
            "description": "Potential to disrupt current business model or industry"
        },
        "opportunity_value": {
            "weight": 0.15,
            "description": "Potential upside if acted upon proactively"
        },
        "threat_severity": {
            "weight": 0.15,
            "description": "Potential downside if ignored or addressed too late"
        },
        "scope_of_impact": {
            "weight": 0.10,
            "description": "Breadth of organizational units or stakeholders affected"
        },
        "viability_impact": {
            "weight": 0.20,
            "description": "Impact on organizational viability (Adaptability, Resilience, Robustness, Excellence)",
            "sub_criteria": {
                "adaptability": "Ability to sense and respond to change",
                "resilience": "Capacity to absorb shocks and recover",
                "robustness": "Strength under varied conditions",
                "operational_excellence": "Efficiency and effectiveness of operations"
            }
        }
    }
    
    @staticmethod
    def assess_impact(signal: WeakSignal, 
                     criterion_scores: Dict[str, int]) -> Tuple[float, str]:
        """
        Assess potential impact of a signal.
        
        Args:
            signal: WeakSignal object
            criterion_scores: Dict mapping criteria to scores (1-5)
            
        Returns:
            Tuple of (weighted_score, impact_level)
        """
        weighted_score = sum(
            criterion_scores.get(criterion, 0) * data["weight"]
            for criterion, data in SignalAnalyzer.IMPACT_CRITERIA.items()
        )
        
        if weighted_score >= 4.0:
            impact_level = "Critical"
        elif weighted_score >= 3.0:
            impact_level = "High"
        elif weighted_score >= 2.0:
            impact_level = "Medium"
        else:
            impact_level = "Low"
            
        return weighted_score, impact_level
    
    @staticmethod
    def calculate_priority_score(signal: WeakSignal,
                                 impact_score: float,
                                 urgency_score: int) -> Tuple[float, str]:
        """
        Calculate priority score combining impact and urgency.
        
        Args:
            signal: WeakSignal object
            impact_score: Calculated impact score (0-5)
            urgency_score: Urgency rating (1-5, with 5 being most urgent)
            
        Returns:
            Tuple of (priority_score, priority_level)
        """
        # Priority = Impact * Urgency, normalized
        priority_score = (impact_score * urgency_score) / 5.0
        
        if priority_score >= 4.0:
            priority_level = "Immediate Action"
        elif priority_score >= 3.0:
            priority_level = "High Priority"
        elif priority_score >= 2.0:
            priority_level = "Monitor Actively"
        else:
            priority_level = "Track & Review"
            
        return priority_score, priority_level
    
    @staticmethod
    def identify_related_signals(target_signal: WeakSignal,
                                signal_database: List[WeakSignal],
                                threshold: float = 0.6) -> List[str]:
        """
        Identify signals related to the target signal.
        
        Simple keyword-based matching. In production, this could use
        more sophisticated semantic similarity methods.
        """
        related = []
        
        target_keywords = set(
            target_signal.title.lower().split() + 
            target_signal.description.lower().split()
        )
        
        for signal in signal_database:
            if signal.id == target_signal.id:
                continue
                
            signal_keywords = set(
                signal.title.lower().split() + 
                signal.description.lower().split()
            )
            
            # Calculate Jaccard similarity
            intersection = len(target_keywords & signal_keywords)
            union = len(target_keywords | signal_keywords)
            similarity = intersection / union if union > 0 else 0
            
            if similarity >= threshold:
                related.append(signal.id)
        
        return related
    
    @staticmethod
    def generate_response_options(signal: WeakSignal,
                                  priority_level: str) -> List[Dict[str, str]]:
        """Generate potential response options based on priority and Cynefin domain."""
        
        # Base responses on Cynefin domain (most signals are Complex)
        if signal.cynefin_domain == CynefinDomain.COMPLEX or signal.cynefin_domain == CynefinDomain.CONFUSED:
            base_responses = [
                {
                    "option": "Probe-Sense-Respond Experiment",
                    "description": "Launch small, safe-to-fail experiment to understand signal implications",
                    "cynefin": "Complex domain - avoid extensive analysis, test and learn"
                },
                {
                    "option": "Scenario Development",
                    "description": "Develop multiple future scenarios incorporating this signal",
                    "cynefin": "Complex domain - explore possibility space"
                }
            ]
        elif signal.cynefin_domain == CynefinDomain.CHAOTIC:
            base_responses = [
                {
                    "option": "Immediate Action",
                    "description": "Act immediately to stabilize situation, then assess",
                    "cynefin": "Chaotic domain - act first, sense second"
                }
            ]
        elif signal.cynefin_domain == CynefinDomain.COMPLICATED:
            base_responses = [
                {
                    "option": "Expert Analysis",
                    "description": "Engage domain experts for thorough analysis",
                    "cynefin": "Complicated domain - analyze before acting"
                }
            ]
        else:  # CLEAR
            base_responses = [
                {
                    "option": "Apply Best Practice",
                    "description": "Implement known best practice response",
                    "cynefin": "Clear domain - standard response"
                }
            ]
        
        response_map = {
            "Immediate Action": base_responses + [
                {
                    "option": "Fast-track strategic review",
                    "description": "Initiate immediate strategic assessment with senior leadership"
                },
                {
                    "option": "Form response team",
                    "description": "Assemble cross-functional team to develop action plan"
                },
                {
                    "option": "Allocate resources",
                    "description": "Dedicate budget and personnel to explore or address signal"
                }
            ],
            "High Priority": base_responses + [
                {
                    "option": "Deep dive analysis",
                    "description": "Conduct thorough research and scenario planning"
                },
                {
                    "option": "Stakeholder engagement",
                    "description": "Consult with internal and external experts"
                }
            ],
            "Monitor Actively": base_responses + [
                {
                    "option": "Regular monitoring",
                    "description": "Schedule periodic reviews and updates"
                },
                {
                    "option": "Expand sources",
                    "description": "Broaden information sources to track signal evolution"
                }
            ],
            "Track & Review": [
                {
                    "option": "Add to radar",
                    "description": "Include in quarterly horizon scanning reviews"
                },
                {
                    "option": "Set triggers",
                    "description": "Define conditions that would elevate priority"
                },
                {
                    "option": "Knowledge sharing",
                    "description": "Share signal information across organization"
                }
            ]
        }
        
        return response_map.get(priority_level, base_responses)
    
    @staticmethod
    def generate_narrative(signal: WeakSignal,
                          impact_level: str,
                          priority_level: str,
                          response_options: List[Dict[str, str]]) -> str:
        """
        Generate compelling narrative about the signal.
        
        Stories accelerate sensemaking and drive action more effectively than data.
        Structure: What, Why, Where, How
        """
        narrative = f"# Signal Narrative: {signal.title}\n\n"
        
        # WHAT: The observed pattern
        narrative += f"## What We're Seeing\n\n"
        narrative += f"{signal.description}\n\n"
        narrative += f"**Signal Strength**: {signal.strength.name.replace('_', ' ').title()}\n"
        narrative += f"**Sources**: {', '.join(signal.sources[:3])}"
        if len(signal.sources) > 3:
            narrative += f" (+{len(signal.sources)-3} more)"
        narrative += f"\n**First Observed**: {signal.first_observed}\n\n"
        
        # WHY: Strategic implications
        narrative += f"## Why This Matters\n\n"
        narrative += f"**Impact Level**: {impact_level}\n"
        narrative += f"**Priority**: {priority_level}\n\n"
        
        if signal.viability_impact and any(signal.viability_impact.values()):
            narrative += "**Impact on Organizational Viability**:\n"
            for pillar, impact in signal.viability_impact.items():
                if impact:
                    narrative += f"- {pillar.replace('_', ' ').title()}: {impact}/5\n"
            narrative += "\n"
        
        # WHERE: Connection to strategy
        narrative += f"## Strategic Connections\n\n"
        narrative += f"This signal relates to our **{signal.signal_type.value}** "
        narrative += f"strategic landscape with implications across **{signal.time_horizon.value if signal.time_horizon else 'undefined timeline'}**.\n\n"
        
        if signal.related_signals:
            narrative += f"**Related Signals**: This connects to {len(signal.related_signals)} other signals in our system, "
            narrative += "suggesting a broader pattern that demands attention.\n\n"
        
        # HOW: Recommended response
        narrative += f"## How to Respond\n\n"
        narrative += f"**Cynefin Domain**: {signal.cynefin_domain.value.title()}\n"
        narrative += f"**Response Pattern**: {signal.response_pattern.value.replace('_', '-').title()}\n\n"
        
        narrative += "**Recommended Actions**:\n\n"
        for i, option in enumerate(response_options[:3], 1):
            narrative += f"{i}. **{option['option']}**: {option['description']}\n"
            if 'cynefin' in option:
                narrative += f"   *({option['cynefin']})*\n"
        
        narrative += f"\n---\n*Signal ID: {signal.id} | Last Updated: {signal.last_updated}*"
        
        return narrative


class SignalRepository:
    """Simple repository for managing weak signals."""
    
    def __init__(self, filepath: str = "signals_database.json"):
        self.filepath = filepath
        self.signals: List[WeakSignal] = []
        
    def add_signal(self, signal: WeakSignal):
        """Add signal to repository."""
        self.signals.append(signal)
        
    def get_signal(self, signal_id: str) -> Optional[WeakSignal]:
        """Retrieve signal by ID."""
        for signal in self.signals:
            if signal.id == signal_id:
                return signal
        return None
    
    def save(self):
        """Save signals to file."""
        data = [signal.to_dict() for signal in self.signals]
        with open(self.filepath, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load(self):
        """Load signals from file."""
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)
                # Reconstruct WeakSignal objects
                # (Simplified - in production, would need full deserialization)
                self.signals = []
                for item in data:
                    signal = WeakSignal(
                        title=item['title'],
                        description=item['description'],
                        signal_type=SignalType(item['signal_type']),
                        sources=item['sources'],
                        first_observed=item['first_observed'],
                        observer=item['observer']
                    )
                    signal.id = item['id']
                    self.signals.append(signal)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    # Example usage
    print("=" * 60)
    print("WEAK SIGNAL CLASSIFICATION FRAMEWORK")
    print("Based on The Tautai Principle")
    print("=" * 60)
    
    # Create example signal
    signal = WeakSignal(
        title="Declining engagement with traditional social media among Gen Z",
        description="Multiple sources indicate Gen Z users are reducing time on "
                   "traditional social media platforms in favor of private "
                   "messaging and ephemeral content",
        signal_type=SignalType.SOCIAL,
        sources=[
            "Pew Research Study Q3 2024",
            "Industry analyst reports",
            "Internal user research"
        ],
        first_observed="2024-09-15",
        observer="Digital Strategy Team"
    )
    
    # Set Cynefin domain (most weak signals are Complex)
    signal.cynefin_domain = CynefinDomain.COMPLEX
    signal.response_pattern = ResponsePattern.PROBE_SENSE_RESPOND
    signal.time_horizon = TimeHorizon.SHORT_TERM
    
    print(f"\nSignal ID: {signal.id}")
    print(f"Title: {signal.title}")
    print(f"Type: {signal.signal_type.value}")
    print(f"Initial Strength: {signal.strength.name}")
    print(f"Cynefin Domain: {signal.cynefin_domain.value.title()}")
    print(f"Response Pattern: {signal.response_pattern.value.replace('_', '-').title()}")
    print(f"Sources: {len(signal.sources)}")
    
    # Assess impact
    criterion_scores = {
        "strategic_relevance": 4,
        "disruptive_potential": 4,
        "opportunity_value": 3,
        "threat_severity": 4,
        "scope_of_impact": 3,
        "viability_impact": 4
    }
    
    # Set viability impact
    signal.viability_impact = {
        "adaptability": 5,  # High impact on ability to sense and respond
        "resilience": 3,    # Moderate impact on recovery capacity
        "robustness": 2,    # Lower impact on strength
        "operational_excellence": 3  # Moderate operational impact
    }
    
    impact_score, impact_level = SignalAnalyzer.assess_impact(signal, criterion_scores)
    print(f"\nImpact Score: {impact_score:.2f}/5.0")
    print(f"Impact Level: {impact_level}")
    
    # Calculate priority
    urgency_score = 3  # Medium term concern
    priority_score, priority_level = SignalAnalyzer.calculate_priority_score(
        signal, impact_score, urgency_score
    )
    print(f"\nPriority Score: {priority_score:.2f}/5.0")
    print(f"Priority Level: {priority_level}")
    
    # Generate response options
    options = SignalAnalyzer.generate_response_options(signal, priority_level)
    
    # Generate narrative (THE KEY OUTPUT)
    print("\n" + "=" * 60)
    print("SIGNAL NARRATIVE (Primary Output)")
    print("=" * 60)
    narrative = SignalAnalyzer.generate_narrative(signal, impact_level, priority_level, options)
    print("\n" + narrative)
    
    print("\n" + "=" * 60)
    print("\nRemember: The narrative is the primary output.")
    print("Stories preserve context and accelerate sensemaking.")
    print("Share this narrative, not just the classification data.")
