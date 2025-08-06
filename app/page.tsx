'use client'

import { useState } from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Label } from '@/components/ui/label'
import { Slider } from '@/components/ui/slider'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { RadioGroup, RadioGroupItem } from '@/components/ui/radio-group'
import { Alert, AlertDescription } from '@/components/ui/alert'
import { Heart, Activity, AlertTriangle, CheckCircle, Stethoscope, Upload } from 'lucide-react'

export default function HeartDiseasePredictor() {
  // State variables matching your original logic
  const [age, setAge] = useState(40)
  const [sex, setSex] = useState('')
  const [chestPain, setChestPain] = useState('')
  const [restingBP, setRestingBP] = useState(80)
  const [cholesterol, setCholesterol] = useState(200)
  const [fastingBS, setFastingBS] = useState('')
  const [restingECG, setRestingECG] = useState('')
  const [maxHR, setMaxHR] = useState(150)
  const [exerciseAngina, setExerciseAngina] = useState('')
  const [oldPeak, setOldPeak] = useState(1.0)
  const [stSlope, setSTSlope] = useState('')
  const [prediction, setPrediction] = useState<number | null>(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  // Prediction function that calls your actual model
  const predictHeartDisease = async () => {
    setIsLoading(true)
    setError(null)
    
    try {
      // Your original logic for creating raw_input
      const rawInput = {
        'Age': age,
        'RestingBP': restingBP,
        'Cholesterol': cholesterol,
        'FastingBS': fastingBS === 'Yes' ? 1 : 0,
        'MaxHR': maxHR,
        'Oldpeak': oldPeak,
        [`Sex_${sex}`]: 1,
        [`ChestPainType_${chestPain}`]: 1,
        [`RestingECG_${restingECG}`]: 1,
        [`ExcerciseAngina_${exerciseAngina}`]: 1,
        [`ST_slope_${stSlope}`]: 1
      }

      // Call the API endpoint with your model
      const response = await fetch('/api/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(rawInput),
      })

      if (!response.ok) {
        throw new Error('Prediction failed. Please try again.')
      }

      const result = await response.json()
      setPrediction(result.prediction)
      
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred during prediction')
    } finally {
      setIsLoading(false)
    }
  }

  const handlePredict = () => {
    if (!sex || !chestPain || !fastingBS || !restingECG || !exerciseAngina || !stSlope) {
      setError('Please fill in all required fields')
      return
    }
    predictHeartDisease()
  }

  const resetForm = () => {
    setAge(40)
    setSex('')
    setChestPain('')
    setRestingBP(80)
    setCholesterol(200)
    setFastingBS('')
    setRestingECG('')
    setMaxHR(150)
    setExerciseAngina('')
    setOldPeak(1.0)
    setSTSlope('')
    setPrediction(null)
    setError(null)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-8 px-4">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-center mb-4">
            <Heart className="h-12 w-12 text-red-500 mr-3" />
            <h1 className="text-4xl font-bold text-gray-900">Heart Disease Prediction</h1>
          </div>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            Advanced AI-powered assessment to evaluate your cardiovascular health risk based on clinical parameters
          </p>
        </div>

        <div className="grid lg:grid-cols-3 gap-8">
          {/* Input Form */}
          <div className="lg:col-span-2 space-y-6">
            {/* Demographics */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center">
                  <Activity className="h-5 w-5 mr-2 text-blue-600" />
                  Demographics
                </CardTitle>
                <CardDescription>Basic demographic information</CardDescription>
              </CardHeader>
              <CardContent className="space-y-6">
                <div className="grid md:grid-cols-2 gap-6">
                  <div className="space-y-3">
                    <Label className="text-sm font-medium">Age: {age} years</Label>
                    <p className="text-xs text-gray-500 mb-2">Age should be greater than or equal to 18</p>
                    <Slider
                      value={[age]}
                      onValueChange={(value) => setAge(value[0])}
                      min={18}
                      max={100}
                      step={1}
                      className="w-full"
                    />
                  </div>
                  <div className="space-y-3">
                    <Label className="text-sm font-medium">Gender</Label>
                    <Select value={sex} onValueChange={setSex}>
                      <SelectTrigger>
                        <SelectValue placeholder="Select gender" />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="M">Male</SelectItem>
                        <SelectItem value="F">Female</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Vital Signs */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center">
                  <Stethoscope className="h-5 w-5 mr-2 text-green-600" />
                  Vital Signs & Lab Results
                </CardTitle>
                <CardDescription>Blood pressure, cholesterol, and other measurements</CardDescription>
              </CardHeader>
              <CardContent className="space-y-6">
                <div className="grid md:grid-cols-2 gap-6">
                  <div className="space-y-3">
                    <Label className="text-sm font-medium">Resting Blood Pressure: {restingBP} mm Hg</Label>
                    <Slider
                      value={[restingBP]}
                      onValueChange={(value) => setRestingBP(value[0])}
                      min={40}
                      max={200}
                      step={1}
                      className="w-full"
                    />
                  </div>
                  <div className="space-y-3">
                    <Label className="text-sm font-medium">Cholesterol: {cholesterol} mg/dL</Label>
                    <Slider
                      value={[cholesterol]}
                      onValueChange={(value) => setCholesterol(value[0])}
                      min={100}
                      max={650}
                      step={1}
                      className="w-full"
                    />
                  </div>
                  <div className="space-y-3">
                    <Label className="text-sm font-medium">Maximum Heart Rate: {maxHR} bpm</Label>
                    <Slider
                      value={[maxHR]}
                      onValueChange={(value) => setMaxHR(value[0])}
                      min={60}
                      max={220}
                      step={1}
                      className="w-full"
                    />
                  </div>
                  <div className="space-y-3">
                    <Label className="text-sm font-medium">Oldpeak (ST Depression): {oldPeak}</Label>
                    <Slider
                      value={[oldPeak]}
                      onValueChange={(value) => setOldPeak(value[0])}
                      min={0}
                      max={6}
                      step={0.1}
                      className="w-full"
                    />
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Clinical Parameters */}
            <Card>
              <CardHeader>
                <CardTitle>Clinical Parameters</CardTitle>
                <CardDescription>Symptoms and diagnostic test results</CardDescription>
              </CardHeader>
              <CardContent className="space-y-6">
                <div className="grid md:grid-cols-2 gap-6">
                  <div className="space-y-3">
                    <Label className="text-sm font-medium">Chest Pain Type</Label>
                    <Select value={chestPain} onValueChange={setChestPain}>
                      <SelectTrigger>
                        <SelectValue placeholder="Select chest pain type" />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="ATA">Atypical Angina</SelectItem>
                        <SelectItem value="NAP">Non-Anginal Pain</SelectItem>
                        <SelectItem value="TA">Typical Angina</SelectItem>
                        <SelectItem value="ASY">Asymptomatic</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                  <div className="space-y-3">
                    <Label className="text-sm font-medium">ST Slope</Label>
                    <Select value={stSlope} onValueChange={setSTSlope}>
                      <SelectTrigger>
                        <SelectValue placeholder="Select ST slope" />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="Up">Upsloping</SelectItem>
                        <SelectItem value="Down">Downsloping</SelectItem>
                        <SelectItem value="Flat">Flat</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                </div>

                <div className="space-y-4">
                  <div>
                    <Label className="text-sm font-medium mb-3 block">Fasting Blood Sugar ≥ 120 mg/dL</Label>
                    <RadioGroup value={fastingBS} onValueChange={setFastingBS} className="flex space-x-6">
                      <div className="flex items-center space-x-2">
                        <RadioGroupItem value="Yes" id="fasting-yes" />
                        <Label htmlFor="fasting-yes">Yes</Label>
                      </div>
                      <div className="flex items-center space-x-2">
                        <RadioGroupItem value="No" id="fasting-no" />
                        <Label htmlFor="fasting-no">No</Label>
                      </div>
                    </RadioGroup>
                  </div>

                  <div>
                    <Label className="text-sm font-medium mb-3 block">Resting ECG</Label>
                    <RadioGroup value={restingECG} onValueChange={setRestingECG} className="flex space-x-6">
                      <div className="flex items-center space-x-2">
                        <RadioGroupItem value="Normal" id="ecg-normal" />
                        <Label htmlFor="ecg-normal">Normal</Label>
                      </div>
                      <div className="flex items-center space-x-2">
                        <RadioGroupItem value="ST" id="ecg-st" />
                        <Label htmlFor="ecg-st">ST-T Wave Abnormality</Label>
                      </div>
                      <div className="flex items-center space-x-2">
                        <RadioGroupItem value="LVH" id="ecg-lvh" />
                        <Label htmlFor="ecg-lvh">Left Ventricular Hypertrophy</Label>
                      </div>
                    </RadioGroup>
                  </div>

                  <div>
                    <Label className="text-sm font-medium mb-3 block">Exercise Induced Angina</Label>
                    <RadioGroup value={exerciseAngina} onValueChange={setExerciseAngina} className="flex space-x-6">
                      <div className="flex items-center space-x-2">
                        <RadioGroupItem value="Y" id="angina-yes" />
                        <Label htmlFor="angina-yes">Yes</Label>
                      </div>
                      <div className="flex items-center space-x-2">
                        <RadioGroupItem value="N" id="angina-no" />
                        <Label htmlFor="angina-no">No</Label>
                      </div>
                    </RadioGroup>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Action Buttons */}
            <div className="flex space-x-4">
              <Button 
                onClick={handlePredict} 
                disabled={isLoading}
                className="flex-1 bg-blue-600 hover:bg-blue-700 text-white py-3"
              >
                {isLoading ? (
                  <>
                    <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
                    Analyzing...
                  </>
                ) : (
                  <>
                    <Heart className="h-4 w-4 mr-2" />
                    Predict Risk
                  </>
                )}
              </Button>
              <Button 
                onClick={resetForm} 
                variant="outline"
                className="px-8"
              >
                Reset
              </Button>
            </div>
          </div>

          {/* Results Panel */}
          <div className="lg:col-span-1">
            <Card className="sticky top-8">
              <CardHeader>
                <CardTitle>Risk Assessment</CardTitle>
                <CardDescription>AI-powered heart disease risk evaluation</CardDescription>
              </CardHeader>
              <CardContent>
                {error && (
                  <Alert className="border-red-200 bg-red-50 mb-4">
                    <AlertTriangle className="h-4 w-4 text-red-600" />
                    <AlertDescription className="text-red-800">
                      {error}
                    </AlertDescription>
                  </Alert>
                )}

                {prediction === null ? (
                  <div className="text-center py-8">
                    <Heart className="h-16 w-16 text-gray-300 mx-auto mb-4" />
                    <p className="text-gray-500">Complete the form and click "Predict Risk" to see your assessment</p>
                  </div>
                ) : (
                  <div className="space-y-4">
                    {prediction === 1 ? (
                      <Alert className="border-red-200 bg-red-50">
                        <AlertTriangle className="h-4 w-4 text-red-600" />
                        <AlertDescription className="text-red-800 font-medium">
                          ⚠️ High Risk of Heart Disease
                        </AlertDescription>
                      </Alert>
                    ) : (
                      <Alert className="border-green-200 bg-green-50">
                        <CheckCircle className="h-4 w-4 text-green-600" />
                        <AlertDescription className="text-green-800 font-medium">
                          ✅ Low Risk of Heart Disease
                        </AlertDescription>
                      </Alert>
                    )}
                    
                    <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                      <p className="text-sm text-gray-600">
                        Created by Anujot Singh
                      </p>
                    </div>
                  </div>
                )}
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  )
}
