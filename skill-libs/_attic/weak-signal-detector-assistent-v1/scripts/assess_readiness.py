#!/usr/bin/env python3
"""
Organizational Readiness Assessment for Weak Signal Detection

This script provides a structured assessment framework to evaluate
an organization's readiness for implementing weak signal detection capabilities.
"""

import json
from typing import Dict, List, Tuple
from datetime import datetime


class ReadinessAssessment:
    """Framework for assessing organizational readiness for weak signal detection."""
    
    DIMENSIONS = {
        "cultural": {
            "name": "Cultural Readiness",
            "weight": 0.30,
            "factors": [
                "psychological_safety",
                "curiosity_orientation",
                "openness_to_challenge",
                "tolerance_for_ambiguity",
                "learning_culture"
            ]
        },
        "structural": {
            "name": "Structural Readiness",
            "weight": 0.25,
            "factors": [
                "cross_functional_communication",
                "information_flow",
                "decision_making_autonomy",
                "peripheral_vision_mechanisms",
                "boundary_spanning_roles"
            ]
        },
        "cognitive": {
            "name": "Cognitive Readiness",
            "weight": 0.25,
            "factors": [
                "diverse_perspectives",
                "systems_thinking",
                "scenario_planning_capability",
                "pattern_recognition_skills",
                "sense_making_processes"
            ]
        },
        "resource": {
            "name": "Resource Readiness",
            "weight": 0.20,
            "factors": [
                "time_allocation",
                "dedicated_roles",
                "technology_infrastructure",
                "analytical_capabilities",
                "external_network_access"
            ]
        }
    }
    
    MATURITY_LEVELS = {
        1: {"label": "Initial", "description": "Ad-hoc, reactive, no systematic approach"},
        2: {"label": "Developing", "description": "Some awareness, informal practices"},
        3: {"label": "Defined", "description": "Established processes, inconsistent application"},
        4: {"label": "Managed", "description": "Systematic approach, regular practice"},
        5: {"label": "Optimizing", "description": "Continuous improvement, integrated culture"}
    }
    
    def __init__(self):
        self.scores: Dict[str, Dict[str, int]] = {}
        self.overall_score: float = 0.0
        self.maturity_level: int = 0
        
    def calculate_dimension_score(self, dimension: str, factor_scores: Dict[str, int]) -> float:
        """Calculate weighted score for a dimension."""
        if not factor_scores:
            return 0.0
        return sum(factor_scores.values()) / len(factor_scores)
    
    def calculate_overall_readiness(self, dimension_scores: Dict[str, float]) -> Tuple[float, int]:
        """Calculate overall readiness score and maturity level."""
        weighted_score = sum(
            dimension_scores[dim] * self.DIMENSIONS[dim]["weight"]
            for dim in dimension_scores
        )
        maturity_level = round(weighted_score)
        return weighted_score, maturity_level
    
    def generate_recommendations(self, dimension_scores: Dict[str, float]) -> List[str]:
        """Generate prioritized recommendations based on assessment."""
        recommendations = []
        
        # Prioritize dimensions below threshold (< 3.0)
        weak_dimensions = {
            dim: score for dim, score in dimension_scores.items() 
            if score < 3.0
        }
        
        if weak_dimensions:
            sorted_dims = sorted(weak_dimensions.items(), key=lambda x: x[1])
            
            for dim, score in sorted_dims[:2]:  # Top 2 priorities
                dim_name = self.DIMENSIONS[dim]["name"]
                recommendations.append(
                    f"**Priority: Strengthen {dim_name}** (Current score: {score:.1f}/5.0)"
                )
                recommendations.extend(self._get_dimension_recommendations(dim))
        
        # Add general recommendations
        if all(score >= 3.0 for score in dimension_scores.values()):
            recommendations.append(
                "**Good foundation detected.** Focus on integration and sustainability."
            )
        
        return recommendations
    
    def _get_dimension_recommendations(self, dimension: str) -> List[str]:
        """Get specific recommendations for a dimension."""
        recommendations_map = {
            "cultural": [
                "- Establish safe spaces for sharing unconventional observations",
                "- Recognize and reward curiosity and exploratory behavior",
                "- Create forums for challenging assumptions without repercussions"
            ],
            "structural": [
                "- Design cross-functional scanning teams or communities of practice",
                "- Implement peripheral vision roles (horizon scanners, trend analysts)",
                "- Create information-sharing platforms that cross silos"
            ],
            "cognitive": [
                "- Build diverse scanning teams with varied backgrounds",
                "- Train staff in systems thinking and futures methodologies",
                "- Establish regular sense-making sessions to interpret signals"
            ],
            "resource": [
                "- Allocate dedicated time for scanning activities (10-20% of roles)",
                "- Invest in scanning tools and information sources",
                "- Provide training in weak signal identification and analysis"
            ]
        }
        return recommendations_map.get(dimension, [])
    
    def generate_report(self, 
                       dimension_scores: Dict[str, float],
                       factor_scores: Dict[str, Dict[str, int]],
                       organization_name: str = "Organization") -> Dict:
        """Generate comprehensive assessment report."""
        overall_score, maturity_level = self.calculate_overall_readiness(dimension_scores)
        recommendations = self.generate_recommendations(dimension_scores)
        
        report = {
            "metadata": {
                "organization": organization_name,
                "assessment_date": datetime.now().isoformat(),
                "version": "1.0"
            },
            "summary": {
                "overall_score": round(overall_score, 2),
                "maturity_level": maturity_level,
                "maturity_label": self.MATURITY_LEVELS[maturity_level]["label"],
                "maturity_description": self.MATURITY_LEVELS[maturity_level]["description"]
            },
            "dimension_scores": {
                dim: {
                    "score": round(score, 2),
                    "weight": self.DIMENSIONS[dim]["weight"],
                    "weighted_contribution": round(score * self.DIMENSIONS[dim]["weight"], 2)
                }
                for dim, score in dimension_scores.items()
            },
            "detailed_scores": factor_scores,
            "recommendations": recommendations,
            "next_steps": self._generate_next_steps(maturity_level)
        }
        
        return report
    
    def _generate_next_steps(self, maturity_level: int) -> List[str]:
        """Generate maturity-appropriate next steps."""
        next_steps_map = {
            1: [
                "Conduct awareness workshops on weak signal detection",
                "Identify potential champions and early adopters",
                "Start small pilot scanning initiatives in receptive units"
            ],
            2: [
                "Formalize scanning processes and responsibilities",
                "Establish regular review cadences for signal sharing",
                "Build connections to external information sources"
            ],
            3: [
                "Standardize methodologies across the organization",
                "Integrate weak signal detection into strategic planning",
                "Develop metrics to track scanning effectiveness"
            ],
            4: [
                "Optimize scanning-action linkages",
                "Build predictive capabilities and scenario planning",
                "Share best practices across organizational units"
            ],
            5: [
                "Lead industry practices in foresight capabilities",
                "Continuously experiment with emerging scanning methods",
                "Mentor other organizations in weak signal detection"
            ]
        }
        return next_steps_map.get(maturity_level, [])


def save_assessment_report(report: Dict, filepath: str = "readiness_assessment.json"):
    """Save assessment report to JSON file."""
    with open(filepath, 'w') as f:
        json.dump(report, indent=2, fp=f)
    return filepath


if __name__ == "__main__":
    # Example usage
    assessor = ReadinessAssessment()
    
    # Example scores (in practice, these would come from structured interviews/surveys)
    example_scores = {
        "cultural": {
            "psychological_safety": 3,
            "curiosity_orientation": 2,
            "openness_to_challenge": 3,
            "tolerance_for_ambiguity": 2,
            "learning_culture": 3
        },
        "structural": {
            "cross_functional_communication": 2,
            "information_flow": 3,
            "decision_making_autonomy": 3,
            "peripheral_vision_mechanisms": 1,
            "boundary_spanning_roles": 2
        },
        "cognitive": {
            "diverse_perspectives": 3,
            "systems_thinking": 2,
            "scenario_planning_capability": 2,
            "pattern_recognition_skills": 3,
            "sense_making_processes": 2
        },
        "resource": {
            "time_allocation": 2,
            "dedicated_roles": 1,
            "technology_infrastructure": 3,
            "analytical_capabilities": 3,
            "external_network_access": 2
        }
    }
    
    # Calculate dimension scores
    dimension_scores = {
        dim: assessor.calculate_dimension_score(dim, example_scores[dim])
        for dim in example_scores
    }
    
    # Generate report
    report = assessor.generate_report(dimension_scores, example_scores, "Example Corp")
    
    # Print summary
    print("=" * 60)
    print("ORGANIZATIONAL READINESS ASSESSMENT")
    print("=" * 60)
    print(f"\nOrganization: {report['metadata']['organization']}")
    print(f"Overall Score: {report['summary']['overall_score']}/5.0")
    print(f"Maturity Level: {report['summary']['maturity_level']} - {report['summary']['maturity_label']}")
    print(f"Description: {report['summary']['maturity_description']}")
    
    print("\n" + "=" * 60)
    print("DIMENSION SCORES")
    print("=" * 60)
    for dim, data in report['dimension_scores'].items():
        dim_name = assessor.DIMENSIONS[dim]["name"]
        print(f"{dim_name:.<30} {data['score']:.2f}/5.0")
    
    print("\n" + "=" * 60)
    print("RECOMMENDATIONS")
    print("=" * 60)
    for rec in report['recommendations']:
        print(rec)
