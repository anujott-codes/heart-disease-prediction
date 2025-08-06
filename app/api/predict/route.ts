import { NextRequest, NextResponse } from 'next/server'

export async function POST(request: NextRequest) {
  try {
    const rawInput = await request.json()
    
    // Call the Python Flask service
    const pythonServiceUrl = process.env.PYTHON_SERVICE_URL || 'http://localhost:5000'
    
    const response = await fetch(`${pythonServiceUrl}/predict`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(rawInput),
    })
    
    if (!response.ok) {
      throw new Error('Python service request failed')
    }
    
    const result = await response.json()
    
    return NextResponse.json(result)
    
  } catch (error) {
    console.error('Prediction error:', error)
    return NextResponse.json(
      { error: 'Failed to make prediction' },
      { status: 500 }
    )
  }
}
